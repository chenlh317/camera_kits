#!/usr/bin/env python3
"""
Analyze focal lengths of JPG photos in a folder and calculate 35mm equivalents.
Generates a summary report including frequency distributions.

Requires: pandas, Pillow

Usage:
    python analyze_focal_lengths.py "<folder_path>"
    If no folder_path is provided, prompts the user for input.

"""

import sys
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime
import pandas as pd
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
    """Extract EXIF data from an image file."""
    try:
        image: Image.Image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data is None:
            return None

        exif = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            exif[tag] = value
        return exif
    except Exception as e:
        print(f"Error reading {image_path}: {e}")
        return None


def calculate_35mm_equivalent(
    focal_length: float,
    exif: Dict[str, Any],
) -> Optional[float]:
    """
    Calculate 35mm equivalent focal length.

    Args:
        focal_length: Actual focal length in mm
        exif: EXIF data dictionary

    Returns:
        35mm equivalent focal length or None
    """
    # Try to get 35mm equivalent directly from EXIF
    if "FocalLengthIn35mmFilm" in exif and exif["FocalLengthIn35mmFilm"]:
        return float(exif["FocalLengthIn35mmFilm"])

    # If not available, try to calculate from crop factor
    # This requires sensor size information which may not always be available
    # For now, return the actual focal length if we can't determine equivalent
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

        # Collect row data
        data.append(
            {
                "Filename": jpg_file.name,
                "Actual Focal Length (mm)": round(focal_length, 1),
                "35mm Equivalent (mm)": (
                    round(equiv_35mm) if equiv_35mm is not None else None
                ),
            }
        )

    # Create DataFrame
    if not data:
        print("\nNo photos with focal length data found in this folder.")
        if files_without_data:
            print(f"Files without focal length data: {len(files_without_data)}")
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
    }

    # Add 35mm equivalent column if available
    if df["35mm Equivalent (mm)"].notna().any():
        equiv_df = df[df["35mm Equivalent (mm)"].notna()]
        summary_data["35mm Equivalent"] = [
            len(equiv_df),
            equiv_df["35mm Equivalent (mm)"].min(),
            equiv_df["35mm Equivalent (mm)"].max(),
            equiv_df["35mm Equivalent (mm)"].mean(),
            equiv_df["35mm Equivalent (mm)"].median(),
        ]

    summary_df = pd.DataFrame(summary_data)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"\n{summary_df.to_string(index=False)}")

    # Frequency distribution for 35mm equivalent
    if df["35mm Equivalent (mm)"].notna().any():
        equiv_df = df[df["35mm Equivalent (mm)"].notna()]
        freq = equiv_df["35mm Equivalent (mm)"].value_counts().sort_index()
        freq_df = pd.DataFrame({"Focal Length (mm)": freq.index, "Count": freq.values})
        # Add percentage share and cumulative percentage
        total_count = freq_df["Count"].sum()
        freq_df["Percentage (%)"] = (freq_df["Count"] / total_count * 100).round(2)
        freq_df["Cumulative (%)"] = freq_df["Percentage (%)"].cumsum().round(2)

        print("\n35mm Equivalent Frequency Distribution:")
        print(freq_df.to_string(index=False))

    if files_without_data:
        print(f"\nFiles without focal length data: {len(files_without_data)}")

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
        }

        # Add 35mm equivalent column if available
        if combined_df["35mm Equivalent (mm)"].notna().any():
            equiv_df = combined_df[combined_df["35mm Equivalent (mm)"].notna()]
            summary_data["35mm Equivalent"] = [
                len(equiv_df),
                equiv_df["35mm Equivalent (mm)"].min(),
                equiv_df["35mm Equivalent (mm)"].max(),
                equiv_df["35mm Equivalent (mm)"].mean(),
                equiv_df["35mm Equivalent (mm)"].median(),
            ]

        summary_df = pd.DataFrame(summary_data)

        print("\n" + "=" * 70)
        print("SUMMARY")
        print("=" * 70)
        print(f"\n{summary_df.to_string(index=False)}")

        # Frequency distribution for 35mm equivalent
        if combined_df["35mm Equivalent (mm)"].notna().any():
            equiv_df = combined_df[combined_df["35mm Equivalent (mm)"].notna()]
            freq = equiv_df["35mm Equivalent (mm)"].value_counts().sort_index()
            freq_df = pd.DataFrame(
                {"Focal Length (mm)": freq.index, "Count": freq.values}
            )
            # Add percentage share and cumulative percentage
            total_count = freq_df["Count"].sum()
            freq_df["Percentage (%)"] = (freq_df["Count"] / total_count * 100).round(2)
            freq_df["Cumulative (%)"] = freq_df["Percentage (%)"].cumsum().round(2)

            print("\n35mm Equivalent Frequency Distribution:")
            print(freq_df.to_string(index=False))


def main(folder_path: str) -> None:
    """
    Main entry point.

    Args:
        folder_path: Path to the folder containing JPG photos
    """
    # Generate output filename based on folder name and timestamp
    folder_name = Path(folder_path).name or "root"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    output_filename = f"{folder_name}_{timestamp}.txt"
    # Save to the same folder as this script
    script_dir = Path(__file__).parent
    output_path = Path.joinpath(script_dir, "focal_length_analysis", output_filename)

    # If file already exists, add a counter to keep both files
    if output_path.exists():
        counter = 1
        base_name: str = output_filename.rsplit(".", 1)[0]  # Remove extension
        extension: str = output_filename.rsplit(".", 1)[1]  # Get extension
        while output_path.exists():
            output_filename = f"{base_name}_{counter}.{extension}"
            output_path = script_dir / output_filename
            counter += 1

    # Open file and redirect output to both console and file
    with open(output_path, "w", encoding="utf-8") as f:
        original_stdout = sys.stdout
        sys.stdout = Tee(f)

        try:
            process_folder(folder_path)
            print(f"\n\nReport saved to: {output_path}")
        finally:
            sys.stdout = original_stdout

    print(f"Report saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        folder_path = input("Enter the folder path containing JPG photos: ").strip()
        main(folder_path)
