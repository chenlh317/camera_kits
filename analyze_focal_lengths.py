#!/usr/bin/env python3
"""
Analyze focal lengths of JPG photos in multiple folders and calculate 35mm equivalents.
Generates a summary report including frequency distributions for each folder.

Requires: pandas, Pillow, pyyaml

Usage:
    python analyze_focal_lengths.py

    Reads folder paths from photo_folders.yaml and processes each folder,
    generating a separate analysis report for each.

    You can comment out folders in the YAML file by adding # at the beginning of the line.

"""

import sys
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime
import pandas as pd
import yaml
from PIL import Image
from PIL.ExifTags import TAGS


class Tee:
    """Write to both console and file simultaneously."""

    def __init__(self, file):
        self.file = file
        self.stdout = sys.stdout

    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)

    def flush(self):
        self.file.flush()
        self.stdout.flush()


def get_exif_data(image_path: Path) -> Optional[Dict[str, Any]]:
    """Extract EXIF data from an image file, including sub-IFD data."""
    try:
        with Image.open(image_path) as image:
            # Try the public getexif() method first (more reliable across formats)
            exif_data = image.getexif()
            if exif_data:
                exif = {}
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    exif[tag] = value

                # Also get EXIF sub-IFD data (contains FocalLength, FocalLengthIn35mmFilm, etc.)
                try:
                    from PIL.ExifTags import IFD

                    exif_ifd = exif_data.get_ifd(IFD.Exif)
                    if exif_ifd:
                        for tag_id, value in exif_ifd.items():
                            tag = TAGS.get(tag_id, tag_id)
                            exif[tag] = value
                except (ImportError, AttributeError):
                    # Older Pillow versions may not have IFD
                    pass

                return exif if exif else None

            # Fallback to private _getexif() for older PIL/Pillow versions
            exif_data = image._getexif()
            if exif_data is None:
                return None

            exif = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                exif[tag] = value
            return exif if exif else None
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
        return None


# Global variable to hold crop factors (loaded once)
_crop_factors: Optional[Dict[str, Any]] = None


def load_crop_factors(yaml_path: Path) -> Optional[Dict[str, Any]]:
    """
    Load camera crop factors from YAML file.

    Args:
        yaml_path: Path to the camera_crop_factors.yaml file

    Returns:
        Dictionary with crop factors or None if file not found
    """
    if not yaml_path.exists():
        return None

    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Warning: Could not load crop factors: {e}")
        return None


def get_crop_factors() -> Optional[Dict[str, Any]]:
    """Get the globally loaded crop factors."""
    return _crop_factors


def calculate_35mm_equivalent(
    focal_length: float,
    exif: Dict[str, Any],
) -> Optional[float]:
    """
    Calculate 35mm equivalent focal length.
    Falls back to calculating from actual focal length and crop factor if available.

    Args:
        focal_length: Actual focal length in mm
        exif: EXIF data dictionary

    Returns:
        35mm equivalent focal length or None
    """
    # Try to get 35mm equivalent directly from EXIF
    if "FocalLengthIn35mmFilm" in exif and exif["FocalLengthIn35mmFilm"]:
        return float(exif["FocalLengthIn35mmFilm"])

    # Fallback: calculate from actual focal length and crop factor
    crop_factors = get_crop_factors()
    if crop_factors is None:
        return None

    # Get camera make and model from EXIF
    make = exif.get("Make", "").strip() if exif.get("Make") else ""
    model = exif.get("Model", "").strip() if exif.get("Model") else ""

    if not model:
        return None

    # Look up crop factor by camera key (Make + Model)
    camera_key = f"{make} {model}".strip()

    # Search in crop_factors
    if "cameras" in crop_factors:
        for key, camera_info in crop_factors["cameras"].items():
            # Match by key or by make+model combination
            if key == camera_key or (
                camera_info.get("make", "") == make
                and camera_info.get("model", "") == model
            ):
                crop_factor = camera_info.get("crop_factor")
                if crop_factor:
                    return focal_length * float(crop_factor)

    return None


def process_single_folder(folder: Path) -> Optional[pd.DataFrame]:
    """
    Process all JPG files in a single folder (non-recursive).

    Args:
        folder: Path object of the folder to process

    Returns:
        DataFrame with photo data, or None if no data found
    """
    # Find all JPG files in this folder only (not recursive)
    jpg_files: List[Path] = (
        list(folder.glob("*.jpg"))
        + list(folder.glob("*.JPG"))
        + list(folder.glob("*.jpeg"))
        + list(folder.glob("*.JPEG"))
    )

    if not jpg_files:
        return None

    # Collect data for dataframe
    data: List[Dict[str, Any]] = []
    files_without_data: List[str] = []
    files_without_35mm_equiv: List[str] = []

    for jpg_file in sorted(jpg_files):
        exif = get_exif_data(jpg_file)

        if exif is None:
            files_without_data.append(jpg_file.name)
            continue

        # Get actual focal length
        focal_length: Optional[float] = None
        if "FocalLength" in exif:
            # FocalLength is often stored as a tuple (numerator, denominator)
            fl = exif["FocalLength"]
            if isinstance(fl, tuple):
                focal_length = fl[0] / fl[1] if fl[1] != 0 else None
            else:
                focal_length = float(fl)

        if focal_length is None:
            files_without_data.append(jpg_file.name)
            continue

        # Calculate or get 35mm equivalent
        equiv_35mm = calculate_35mm_equivalent(focal_length, exif)

        # Skip this photo if 35mm equivalent is not available
        if equiv_35mm is None:
            files_without_35mm_equiv.append(jpg_file.name)
            continue

        # Collect row data (only photos with 35mm equivalent)
        data.append(
            {
                "Filename": jpg_file.name,
                "Actual Focal Length (mm)": round(focal_length, 1),
                "35mm Equivalent (mm)": round(equiv_35mm),
            }
        )

    # Create DataFrame
    if not data:
        print(
            "\nNo photos with 35mm equivalent focal length data found in this folder."
        )
        if files_without_data:
            print(f"Files without EXIF/focal length data: {len(files_without_data)}")
        if files_without_35mm_equiv:
            print(
                f"Files without 35mm equivalent data: {len(files_without_35mm_equiv)}"
            )
        return None

    df = pd.DataFrame(data)

    # Create summary dataframe
    summary_data: Dict[str, Any] = {
        "Metric": ["Count", "Min (mm)", "Max (mm)", "Mean (mm)", "Median (mm)"],
        "Actual Focal Length": [
            len(df),
            df["Actual Focal Length (mm)"].min(),
            df["Actual Focal Length (mm)"].max(),
            df["Actual Focal Length (mm)"].mean(),
            df["Actual Focal Length (mm)"].median(),
        ],
        "35mm Equivalent": [
            len(df),
            df["35mm Equivalent (mm)"].min(),
            df["35mm Equivalent (mm)"].max(),
            df["35mm Equivalent (mm)"].mean(),
            df["35mm Equivalent (mm)"].median(),
        ],
    }

    summary_df = pd.DataFrame(summary_data)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"\n{summary_df.to_string(index=False)}")

    # Frequency distribution for 35mm equivalent
    freq = df["35mm Equivalent (mm)"].value_counts().sort_index()
    freq_df = pd.DataFrame({"Focal Length (mm)": freq.index, "Count": freq.values})
    # Add percentage share and cumulative percentage
    total_count = freq_df["Count"].sum()
    freq_df["Percentage (%)"] = (freq_df["Count"] / total_count * 100).round(2)
    freq_df["Cumulative (%)"] = freq_df["Percentage (%)"].cumsum().round(2)

    print("\n35mm Equivalent Frequency Distribution:")
    print(freq_df.to_string(index=False))

    if files_without_data or files_without_35mm_equiv:
        if files_without_data:
            print(f"\nFiles without EXIF/focal length data: {len(files_without_data)}")
        if files_without_35mm_equiv:
            print(
                f"Files without 35mm equivalent data (skipped): {len(files_without_35mm_equiv)}"
            )

    return df


def process_folder(folder_path: str) -> None:
    """
    Process all JPG files in the given folder and all its subfolders.
    Results are summarized separately for each folder.

    Args:
        folder_path: Path to the folder containing photos
    """
    root_folder = Path(folder_path)

    if not root_folder.exists() or not root_folder.is_dir():
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    # Get all folders (root + subfolders)
    all_folders: List[Path] = [root_folder] + [
        d for d in root_folder.rglob("*") if d.is_dir()
    ]

    # Filter to only folders that contain JPG files
    folders_with_photos: List[Path] = []
    for folder in all_folders:
        has_photos: bool = (
            any(folder.glob("*.jpg"))
            or any(folder.glob("*.JPG"))
            or any(folder.glob("*.jpeg"))
            or any(folder.glob("*.JPEG"))
        )
        if has_photos:
            folders_with_photos.append(folder)

    if not folders_with_photos:
        print(f"No JPG files found in '{folder_path}' or its subfolders")
        return

    print(f"Found {len(folders_with_photos)} folder(s) with JPG files")
    print("=" * 70)

    # Collect all dataframes for overall summary
    all_dfs: List[pd.DataFrame] = []

    # Process each folder separately
    for i, folder in enumerate(sorted(folders_with_photos), 1):
        print(f"\n{'#' * 70}")
        print(
            f"# FOLDER {i}/{len(folders_with_photos)}: {folder.relative_to(root_folder) if folder != root_folder else '(root)'}"
        )
        print(f"{'#' * 70}")
        folder_df = process_single_folder(folder)
        if folder_df is not None:
            all_dfs.append(folder_df)

    # Print overall summary across all folders
    if all_dfs:
        print(f"\n\n{'*' * 70}")
        print(f"{'*' * 70}")
        print("OVERALL SUMMARY - ALL FOLDERS COMBINED")
        print(f"{'*' * 70}")
        print(f"{'*' * 70}")

        # Combine all dataframes
        combined_df = pd.concat(all_dfs, ignore_index=True)

        # Create overall summary dataframe
        summary_data: Dict[str, Any] = {
            "Metric": ["Count", "Min (mm)", "Max (mm)", "Mean (mm)", "Median (mm)"],
            "Actual Focal Length": [
                len(combined_df),
                combined_df["Actual Focal Length (mm)"].min(),
                combined_df["Actual Focal Length (mm)"].max(),
                combined_df["Actual Focal Length (mm)"].mean(),
                combined_df["Actual Focal Length (mm)"].median(),
            ],
            "35mm Equivalent": [
                len(combined_df),
                combined_df["35mm Equivalent (mm)"].min(),
                combined_df["35mm Equivalent (mm)"].max(),
                combined_df["35mm Equivalent (mm)"].mean(),
                combined_df["35mm Equivalent (mm)"].median(),
            ],
        }

        summary_df = pd.DataFrame(summary_data)

        print("\n" + "=" * 70)
        print("SUMMARY")
        print("=" * 70)
        print(f"\n{summary_df.to_string(index=False)}")

        # Frequency distribution for 35mm equivalent
        freq = combined_df["35mm Equivalent (mm)"].value_counts().sort_index()
        freq_df = pd.DataFrame({"Focal Length (mm)": freq.index, "Count": freq.values})
        # Add percentage share and cumulative percentage
        total_count = freq_df["Count"].sum()
        freq_df["Percentage (%)"] = (freq_df["Count"] / total_count * 100).round(2)
        freq_df["Cumulative (%)"] = freq_df["Percentage (%)"].cumsum().round(2)

        print("\n35mm Equivalent Frequency Distribution:")
        print(freq_df.to_string(index=False))


def main(folder_path: str, output_dir: Path) -> None:
    """
    Main entry point.

    Args:
        folder_path: Path to the folder containing JPG photos
        output_dir: Directory to save output files
    """
    # Generate output filename based on folder name
    folder_name = Path(folder_path).name or "root"
    output_filename = f"{folder_name}.txt"
    # Save to the output directory
    output_path = output_dir / output_filename

    # If file already exists, add a counter to keep both files
    if output_path.exists():
        counter = 1
        base_name: str = output_filename.rsplit(".", 1)[0]  # Remove extension
        extension: str = output_filename.rsplit(".", 1)[1]  # Get extension
        while output_path.exists():
            output_filename = f"{base_name}_{counter}.{extension}"
            output_path = output_dir / output_filename
            counter += 1

    # Open file and redirect output to both console and file
    with open(output_path, "w", encoding="utf-8") as f:
        original_stdout = sys.stdout
        sys.stdout = Tee(f)

        try:
            print(f"ANALYZING FOLDER: {folder_path}")
            print("=" * 70)
            print()
            process_folder(folder_path)
            print(f"\n\nReport saved to: {output_path}")
        finally:
            sys.stdout = original_stdout

    print(f"Report saved to: {output_path}")


if __name__ == "__main__":
    # Read photo folders from photo_folders.yaml
    script_dir = Path(__file__).parent
    folders_file = script_dir / "photo_folders.yaml"

    if not folders_file.exists():
        print(f"Error: {folders_file} not found!")
        sys.exit(1)

    # Load camera crop factors for fallback calculation
    crop_factors_path = script_dir / "camera_crop_factors.yaml"
    _crop_factors = load_crop_factors(crop_factors_path)
    if _crop_factors:
        print(
            f"Loaded crop factors for {len(_crop_factors.get('cameras', {}))} cameras"
        )
    else:
        print("No crop factors file found, will only use direct EXIF 35mm equivalent")

    # Read all folder paths from the YAML file
    with open(folders_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    folder_paths = config.get("folders", [])

    if not folder_paths:
        print(f"Error: No folder paths found in {folders_file}")
        sys.exit(1)

    print(f"Found {len(folder_paths)} folder(s) to process")

    # Create output directory with timestamp
    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = script_dir / f"focal_length_analysis_{run_timestamp}"
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    # Process each folder
    for i, folder_path in enumerate(folder_paths, 1):
        print(f"\n{'=' * 80}")
        print(f"Processing folder {i}/{len(folder_paths)}: {folder_path}")
        print(f"{'=' * 80}")
        main(folder_path, output_dir)
