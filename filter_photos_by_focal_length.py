#!/usr/bin/env python3
"""
Filter and copy photos by 35mm-equivalent focal length range.

This script:
1. Reads folder directories from photo_folders.yaml
2. Recursively scans each folder and subfolders for photo files
3. Reads EXIF data from each photo file
4. Filters photos by 35mm-equivalent focal length within a given range
5. Copies matching files to a timestamped folder named with the focal length range
6. Renames copied files with source folder name + original filename
7. Writes a detailed log file

Requires: Pillow, pyyaml

Usage:
    python filter_photos_by_focal_length.py
"""

import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml
from PIL import Image
from PIL.ExifTags import TAGS


# Supported image extensions
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".heic", ".heif"}


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
    except Exception:
        return None


def get_35mm_equivalent(exif: Dict[str, Any]) -> Optional[float]:
    """
    Get 35mm equivalent focal length from EXIF data.

    Args:
        exif: EXIF data dictionary

    Returns:
        35mm equivalent focal length or None if not available
    """
    # Try to get 35mm equivalent directly from EXIF
    if "FocalLengthIn35mmFilm" in exif and exif["FocalLengthIn35mmFilm"]:
        return float(exif["FocalLengthIn35mmFilm"])
    return None


def load_folders_from_yaml(yaml_path: Path) -> List[Path]:
    """
    Load folder paths from photo_folders.yaml.

    Args:
        yaml_path: Path to the YAML configuration file

    Returns:
        List of Path objects for folders to process
    """
    if not yaml_path.exists():
        print(f"Error: Configuration file not found: {yaml_path}")
        sys.exit(1)

    with open(yaml_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    folders = []
    if config and "folders" in config:
        for folder_str in config["folders"]:
            if folder_str:  # Skip empty entries
                folder_path = Path(folder_str)
                if folder_path.exists():
                    folders.append(folder_path)
                else:
                    print(f"Warning: Folder not found, skipping: {folder_str}")

    return folders


def find_all_image_files(folder: Path) -> List[Path]:
    """
    Find all image files in a folder and its subfolders recursively.

    Args:
        folder: Root folder to search

    Returns:
        List of Path objects for all image files found
    """
    image_files = []
    for ext in IMAGE_EXTENSIONS:
        # Search for both lowercase and uppercase extensions
        image_files.extend(folder.rglob(f"*{ext}"))
        image_files.extend(folder.rglob(f"*{ext.upper()}"))

    # Remove duplicates and sort
    return sorted(set(image_files))


def sanitize_filename(name: str) -> str:
    """
    Sanitize a string to be safe for use in filenames.

    Args:
        name: Original string

    Returns:
        Sanitized string safe for filenames
    """
    # Replace problematic characters with underscores
    invalid_chars = '<>:"/\\|?*'
    result = name
    for char in invalid_chars:
        result = result.replace(char, "_")
    return result


def create_output_folder(project_root: Path, min_focal: int, max_focal: int) -> Path:
    """
    Create output folder with datetime stamp and focal length range.

    Args:
        project_root: Root directory of the project
        min_focal: Minimum focal length
        max_focal: Maximum focal length

    Returns:
        Path to the created output folder
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"filtered_photos_{timestamp}_{min_focal}mm-{max_focal}mm"
    output_folder = project_root / folder_name
    output_folder.mkdir(parents=True, exist_ok=True)
    return output_folder


def process_photos(
    folders: List[Path],
    min_focal: int,
    max_focal: int,
    output_folder: Path,
    log_file: Path,
) -> Tuple[int, int, int, int]:
    """
    Process all photos in the given folders.

    Args:
        folders: List of folders to process
        min_focal: Minimum 35mm equivalent focal length (inclusive)
        max_focal: Maximum 35mm equivalent focal length (inclusive)
        output_folder: Destination folder for copied files
        log_file: Path to the log file

    Returns:
        Tuple of (total_files_scanned, files_with_exif, files_in_range, files_copied)
    """
    total_files_scanned = 0
    files_with_exif = 0
    files_with_35mm = 0
    files_copied = 0

    copied_files_log: List[Dict[str, str]] = []
    folders_processed: List[Dict[str, Any]] = []

    for folder in folders:
        folder_stats = {
            "path": str(folder),
            "files_scanned": 0,
            "files_with_exif": 0,
            "files_with_35mm": 0,
            "files_matched": 0,
            "subfolders": set(),
        }

        print(f"\nProcessing folder: {folder}")

        # Find all image files recursively
        image_files = find_all_image_files(folder)
        folder_stats["files_scanned"] = len(image_files)
        total_files_scanned += len(image_files)

        if not image_files:
            print("  No image files found")
            folders_processed.append(folder_stats)
            continue

        print(f"  Found {len(image_files)} image files")

        for image_path in image_files:
            # Track subfolders
            relative_path = image_path.relative_to(folder)
            if len(relative_path.parts) > 1:
                subfolder = relative_path.parent
                folder_stats["subfolders"].add(str(subfolder))

            # Get EXIF data
            exif = get_exif_data(image_path)
            if exif is None:
                continue

            folder_stats["files_with_exif"] += 1
            files_with_exif += 1

            # Get 35mm equivalent focal length
            focal_35mm = get_35mm_equivalent(exif)
            if focal_35mm is None:
                continue

            folder_stats["files_with_35mm"] += 1
            files_with_35mm += 1

            # Check if within the specified range
            if min_focal <= focal_35mm <= max_focal:
                folder_stats["files_matched"] += 1

                # Create new filename: source_folder_name + 35mm_focal_length + original_filename
                source_folder_name = sanitize_filename(folder.name)
                focal_str = f"{int(focal_35mm)}mm"

                # If file is in a subfolder, include subfolder info
                if len(relative_path.parts) > 1:
                    subfolder_name = sanitize_filename(
                        str(relative_path.parent).replace("/", "_").replace("\\", "_")
                    )
                    new_filename = (
                        f"{source_folder_name}_{subfolder_name}_{focal_str}_{image_path.name}"
                    )
                else:
                    new_filename = f"{source_folder_name}_{focal_str}_{image_path.name}"

                dest_path = output_folder / new_filename

                # Handle filename conflicts
                counter = 1
                original_stem = dest_path.stem
                while dest_path.exists():
                    dest_path = (
                        output_folder / f"{original_stem}_{counter}{dest_path.suffix}"
                    )
                    counter += 1

                # Copy the file
                try:
                    shutil.copy2(image_path, dest_path)
                    files_copied += 1

                    copied_files_log.append(
                        {
                            "source": str(image_path),
                            "destination": str(dest_path),
                            "focal_length_35mm": focal_35mm,
                        }
                    )

                except Exception as e:
                    print(f"  Error copying {image_path}: {e}")

        # Convert set to list for logging
        folder_stats["subfolders"] = list(folder_stats["subfolders"])
        folders_processed.append(folder_stats)

        print(
            f"  EXIF found: {folder_stats['files_with_exif']}, "
            f"35mm info: {folder_stats['files_with_35mm']}, "
            f"In range: {folder_stats['files_matched']}"
        )

    # Write log file
    write_log_file(
        log_file,
        folders_processed,
        copied_files_log,
        min_focal,
        max_focal,
        total_files_scanned,
        files_with_exif,
        files_with_35mm,
        files_copied,
    )

    return total_files_scanned, files_with_exif, files_with_35mm, files_copied


def write_log_file(
    log_file: Path,
    folders_processed: List[Dict[str, Any]],
    copied_files: List[Dict[str, str]],
    min_focal: int,
    max_focal: int,
    total_scanned: int,
    with_exif: int,
    with_35mm: int,
    copied: int,
) -> None:
    """
    Write detailed log file.

    Args:
        log_file: Path to the log file
        folders_processed: List of folder processing statistics
        copied_files: List of copied file information
        min_focal: Minimum focal length filter
        max_focal: Maximum focal length filter
        total_scanned: Total number of files scanned
        with_exif: Number of files with EXIF data
        with_35mm: Number of files with 35mm equivalent info
        copied: Number of files copied
    """
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("PHOTO FILTER LOG - BY 35MM EQUIVALENT FOCAL LENGTH\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Focal Length Range: {min_focal}mm - {max_focal}mm\n\n")

        # Summary statistics
        f.write("-" * 40 + "\n")
        f.write("SUMMARY\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total folders processed:       {len(folders_processed)}\n")
        f.write(f"Total files scanned:           {total_scanned}\n")
        f.write(f"Files with EXIF data:          {with_exif}\n")
        f.write(f"Files with 35mm equivalent:    {with_35mm}\n")
        f.write(f"Files matching focal range:    {copied}\n\n")

        # Folder details
        f.write("-" * 40 + "\n")
        f.write("FOLDERS PROCESSED\n")
        f.write("-" * 40 + "\n\n")

        for folder_info in folders_processed:
            f.write(f"Folder: {folder_info['path']}\n")
            f.write(f"  Files scanned:      {folder_info['files_scanned']}\n")
            f.write(f"  Files with EXIF:    {folder_info['files_with_exif']}\n")
            f.write(f"  Files with 35mm:    {folder_info['files_with_35mm']}\n")
            f.write(f"  Files matched:      {folder_info['files_matched']}\n")
            if folder_info["subfolders"]:
                f.write(f"  Subfolders visited: {len(folder_info['subfolders'])}\n")
                for sf in sorted(folder_info["subfolders"]):
                    f.write(f"    - {sf}\n")
            f.write("\n")

        # Copied files list
        f.write("-" * 40 + "\n")
        f.write("COPIED FILES\n")
        f.write("-" * 40 + "\n\n")

        if copied_files:
            for file_info in copied_files:
                f.write(f"Source:      {file_info['source']}\n")
                f.write(f"Destination: {file_info['destination']}\n")
                f.write(f"35mm Equiv:  {file_info['focal_length_35mm']}mm\n")
                f.write("\n")
        else:
            f.write("No files matched the specified focal length range.\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("END OF LOG\n")
        f.write("=" * 80 + "\n")


def main(min_focal: int, max_focal: int, config: str = "photo_folders.yaml"):
    """
    Main entry point.

    Args:
        min_focal: Minimum 35mm equivalent focal length (inclusive)
        max_focal: Maximum 35mm equivalent focal length (inclusive)
        config: Path to the YAML configuration file
    """
    if min_focal > max_focal:
        print("Error: Minimum focal length cannot be greater than maximum.")
        sys.exit(1)

    # Get project root directory
    project_root = Path(__file__).parent.resolve()

    # Load configuration
    config_path = project_root / config
    print(f"Loading configuration from: {config_path}")
    folders = load_folders_from_yaml(config_path)

    if not folders:
        print("No valid folders found in configuration file.")
        sys.exit(1)

    print(f"\nFound {len(folders)} folders to process")
    print(f"Filtering photos with 35mm equivalent: {min_focal}mm - {max_focal}mm")

    # Create output folder
    output_folder = create_output_folder(project_root, min_focal, max_focal)
    print(f"\nOutput folder: {output_folder}")

    # Create log file path (same name as folder)
    log_file = output_folder.parent / f"{output_folder.name}.txt"

    # Process photos
    total, with_exif, with_35mm, copied = process_photos(
        folders, min_focal, max_focal, output_folder, log_file
    )

    # Print final summary
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"Total files scanned:        {total}")
    print(f"Files with EXIF data:       {with_exif}")
    print(f"Files with 35mm equivalent: {with_35mm}")
    print(f"Files copied:               {copied}")
    print(f"\nOutput folder: {output_folder}")
    print(f"Log file: {log_file}")

    if copied == 0:
        print("\nNo photos matched the specified focal length range.")
        # Remove empty output folder
        try:
            log_file.unlink()
            output_folder.rmdir()
            print("Empty output folder removed.")
        except Exception:
            pass


if __name__ == "__main__":

    main(
        min_focal=100,
        max_focal=199,
        config="photo_folders.yaml",
    )
