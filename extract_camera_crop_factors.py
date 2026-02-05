#!/usr/bin/env python3
"""
Extract camera/device information from photos and look up crop factors.

This script:
1. Loops through photo files in folders listed in photo_folders.yaml
2. Extracts device/camera info from EXIF data
3. Searches the internet for crop factors for each device/camera
4. Writes the crop factor info to a YAML file

Requires: Pillow, pyyaml, requests, beautifulsoup4

Usage:
    python extract_camera_crop_factors.py
"""

import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import quote_plus

import requests
import yaml
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS


# Common crop factors database (fallback for well-known devices)
KNOWN_CROP_FACTORS: Dict[str, Dict[str, Any]] = {
    # Apple iPhones (various sensor sizes, approximate)
    "Apple iPhone 4": {"crop_factor": 7.61, "sensor_size": "1/3.2 inch"},
    "Apple iPhone 4S": {"crop_factor": 7.61, "sensor_size": "1/3.2 inch"},
    "Apple iPhone 5": {"crop_factor": 7.61, "sensor_size": "1/3.2 inch"},
    "Apple iPhone 5s": {"crop_factor": 7.21, "sensor_size": "1/3 inch"},
    "Apple iPhone 6": {"crop_factor": 7.21, "sensor_size": "1/3 inch"},
    "Apple iPhone 6s": {"crop_factor": 7.21, "sensor_size": "1/3 inch"},
    "Apple iPhone 6 Plus": {"crop_factor": 7.21, "sensor_size": "1/3 inch"},
    "Apple iPhone 6s Plus": {"crop_factor": 7.21, "sensor_size": "1/3 inch"},
    "Apple iPhone 7": {"crop_factor": 5.41, "sensor_size": "1/2.6 inch"},
    "Apple iPhone 7 Plus": {"crop_factor": 5.41, "sensor_size": "1/2.6 inch"},
    "Apple iPhone 8": {"crop_factor": 5.41, "sensor_size": "1/2.6 inch"},
    "Apple iPhone 8 Plus": {"crop_factor": 5.41, "sensor_size": "1/2.6 inch"},
    "Apple iPhone X": {"crop_factor": 5.41, "sensor_size": "1/2.6 inch"},
    "Apple iPhone XS": {"crop_factor": 5.41, "sensor_size": "1/2.55 inch"},
    "Apple iPhone XR": {"crop_factor": 5.41, "sensor_size": "1/2.55 inch"},
    "Apple iPhone 11": {"crop_factor": 5.41, "sensor_size": "1/2.55 inch"},
    "Apple iPhone 11 Pro": {"crop_factor": 5.41, "sensor_size": "1/2.55 inch"},
    "Apple iPhone 12": {"crop_factor": 5.41, "sensor_size": "1/2.55 inch"},
    "Apple iPhone 12 Pro": {"crop_factor": 4.25, "sensor_size": "1/1.76 inch"},
    "Apple iPhone 13": {"crop_factor": 4.25, "sensor_size": "1/1.67 inch"},
    "Apple iPhone 13 Pro": {"crop_factor": 3.93, "sensor_size": "1/1.65 inch"},
    "Apple iPhone 14": {"crop_factor": 3.93, "sensor_size": "1/1.65 inch"},
    "Apple iPhone 14 Pro": {"crop_factor": 2.86, "sensor_size": "1/1.28 inch"},
    "Apple iPhone 15": {"crop_factor": 2.86, "sensor_size": "1/1.28 inch"},
    "Apple iPhone 15 Pro": {"crop_factor": 2.86, "sensor_size": "1/1.28 inch"},
    # Samsung phones
    "samsung SM-S901B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S22"},
    "samsung SM-S901E": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S22"},
    "samsung SM-S906B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S22+"},
    "samsung SM-S908B": {"crop_factor": 2.19, "sensor_size": "1/1.33 inch", "model": "Galaxy S22 Ultra"},
    "samsung SM-S911B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S23"},
    "samsung SM-S916B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S23+"},
    "samsung SM-S918B": {"crop_factor": 2.0, "sensor_size": "1/1.3 inch", "model": "Galaxy S23 Ultra"},
    "samsung SM-S921B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S24"},
    "samsung SM-S926B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S24+"},
    "samsung SM-S928B": {"crop_factor": 2.0, "sensor_size": "1/1.3 inch", "model": "Galaxy S24 Ultra"},
    "samsung SM-S931B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S25"},
    "samsung SM-S936B": {"crop_factor": 3.93, "sensor_size": "1/1.57 inch", "model": "Galaxy S25+"},
    "samsung SM-S938B": {"crop_factor": 2.0, "sensor_size": "1/1.3 inch", "model": "Galaxy S25 Ultra"},
    # Huawei phones
    "HUAWEI ELE-L29": {"crop_factor": 3.93, "sensor_size": "1/1.7 inch", "model": "P30"},
    "HUAWEI VOG-L29": {"crop_factor": 3.93, "sensor_size": "1/1.7 inch", "model": "P30 Pro"},
    "HUAWEI ANA-NX9": {"crop_factor": 3.18, "sensor_size": "1/1.28 inch", "model": "P40"},
    "HUAWEI ANA-LX4": {"crop_factor": 3.18, "sensor_size": "1/1.28 inch", "model": "P40"},
    "HUAWEI ELS-NX9": {"crop_factor": 3.18, "sensor_size": "1/1.28 inch", "model": "P40 Pro"},
    # Nokia phones
    "Nokia 3110c": {"crop_factor": 9.6, "sensor_size": "1/4 inch"},
    "Nokia 6303c": {"crop_factor": 8.65, "sensor_size": "1/3.6 inch"},
    "Nokia E5-00": {"crop_factor": 8.65, "sensor_size": "1/3.6 inch"},
    "Nokia E72": {"crop_factor": 8.65, "sensor_size": "1/3.6 inch"},
    # Samsung older phones
    "SAMSUNG SGH-E488": {"crop_factor": 9.6, "sensor_size": "1/4 inch (estimated)"},
    # Common DSLRs and Mirrorless (APS-C)
    "Canon EOS 7D": {"crop_factor": 1.6, "sensor_size": "APS-C"},
    "Canon EOS 70D": {"crop_factor": 1.6, "sensor_size": "APS-C"},
    "Canon EOS 80D": {"crop_factor": 1.6, "sensor_size": "APS-C"},
    "Canon EOS Rebel": {"crop_factor": 1.6, "sensor_size": "APS-C"},
    "NIKON D3": {"crop_factor": 1.5, "sensor_size": "APS-C"},
    "NIKON D5": {"crop_factor": 1.5, "sensor_size": "APS-C"},
    "NIKON D7": {"crop_factor": 1.5, "sensor_size": "APS-C"},
    "SONY ILCE-6": {"crop_factor": 1.5, "sensor_size": "APS-C"},
    "FUJIFILM X-T": {"crop_factor": 1.5, "sensor_size": "APS-C"},
    # Full frame cameras
    "Canon EOS 5D": {"crop_factor": 1.0, "sensor_size": "Full Frame"},
    "Canon EOS 6D": {"crop_factor": 1.0, "sensor_size": "Full Frame"},
    "Canon EOS R": {"crop_factor": 1.0, "sensor_size": "Full Frame"},
    "NIKON D8": {"crop_factor": 1.0, "sensor_size": "Full Frame"},
    "NIKON Z": {"crop_factor": 1.0, "sensor_size": "Full Frame"},
    "SONY ILCE-7": {"crop_factor": 1.0, "sensor_size": "Full Frame"},
    # Micro Four Thirds
    "OLYMPUS": {"crop_factor": 2.0, "sensor_size": "Micro Four Thirds"},
    "Panasonic DC-G": {"crop_factor": 2.0, "sensor_size": "Micro Four Thirds"},
    "Panasonic DMC-G": {"crop_factor": 2.0, "sensor_size": "Micro Four Thirds"},
}


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


def extract_camera_info(exif: Dict[str, Any]) -> Optional[Tuple[str, str, str]]:
    """
    Extract camera make, model, and combined identifier from EXIF data.

    Returns:
        Tuple of (make, model, combined_identifier) or None
    """
    make = exif.get("Make", "").strip() if exif.get("Make") else ""
    model = exif.get("Model", "").strip() if exif.get("Model") else ""

    if not make and not model:
        return None

    # Clean up make and model
    make = make.replace("\x00", "").strip()
    model = model.replace("\x00", "").strip()

    # Create combined identifier
    if make and model:
        # Avoid duplication if model already contains make
        if make.lower() in model.lower():
            combined = model
        else:
            combined = f"{make} {model}"
    elif model:
        combined = model
    else:
        combined = make

    return (make, model, combined)


def search_crop_factor_online(camera_name: str) -> Optional[Dict[str, Any]]:
    """
    Search for crop factor information online.

    Args:
        camera_name: The camera/device name to search for

    Returns:
        Dictionary with crop_factor and sensor_size, or None
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # Try DuckDuckGo HTML search
    search_query = f"{camera_name} sensor size crop factor specifications"
    url = f"https://html.duckduckgo.com/html/?q={quote_plus(search_query)}"

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Get search result snippets
            results = soup.find_all("a", class_="result__snippet")
            all_text = " ".join([r.get_text() for r in results[:5]])

            # Also check result titles
            titles = soup.find_all("a", class_="result__a")
            all_text += " " + " ".join([t.get_text() for t in titles[:5]])

            # Try to extract crop factor from text
            crop_factor = extract_crop_factor_from_text(all_text)
            sensor_size = extract_sensor_size_from_text(all_text)

            if crop_factor or sensor_size:
                result = {"source": "web_search"}
                if crop_factor:
                    result["crop_factor"] = crop_factor
                if sensor_size:
                    result["sensor_size"] = sensor_size
                    # Calculate crop factor from sensor size if not found directly
                    if not crop_factor:
                        calculated = calculate_crop_factor_from_sensor_size(sensor_size)
                        if calculated:
                            result["crop_factor"] = calculated
                            result["crop_factor_calculated"] = True
                return result if "crop_factor" in result else None

    except Exception as e:
        print(f"  Web search error for {camera_name}: {e}")

    return None


def extract_crop_factor_from_text(text: str) -> Optional[float]:
    """Extract crop factor value from text."""
    text = text.lower()

    # Patterns for crop factor
    patterns = [
        r"crop\s*factor[:\s]+(\d+\.?\d*)",
        r"(\d+\.?\d*)\s*x?\s*crop",
        r"focal\s*length\s*multiplier[:\s]+(\d+\.?\d*)",
        r"(\d+\.?\d*)x\s*focal\s*length",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            try:
                value = float(match.group(1))
                # Reasonable crop factor range
                if 0.5 <= value <= 15:
                    return round(value, 2)
            except ValueError:
                continue

    return None


def extract_sensor_size_from_text(text: str) -> Optional[str]:
    """Extract sensor size from text."""
    # Common sensor size patterns
    patterns = [
        r"(1/\d+\.?\d*[\s-]*inch)",
        r"(1/\d+\.?\d*\")",
        r"(\d+\.?\d*\s*[x×]\s*\d+\.?\d*\s*mm)",
        r"(full\s*frame)",
        r"(aps-c)",
        r"(micro\s*four\s*thirds)",
        r"(m4/3)",
        r"(medium\s*format)",
    ]

    text_lower = text.lower()
    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if match:
            return match.group(1).strip()

    return None


def calculate_crop_factor_from_sensor_size(sensor_size: str) -> Optional[float]:
    """Calculate crop factor from sensor size string."""
    sensor_size_lower = sensor_size.lower()

    # Full frame reference: 43.27mm diagonal
    full_frame_diagonal = 43.27

    # Known sensor sizes and their diagonals
    sensor_diagonals = {
        "full frame": 43.27,
        "aps-c": 28.4,  # Canon APS-C
        "aps-c nikon": 28.4,
        "micro four thirds": 21.6,
        "m4/3": 21.6,
        "1 inch": 15.86,
        "1/1.28 inch": 12.4,
        "1/1.3 inch": 12.3,
        "1/1.33 inch": 12.0,
        "1/1.5 inch": 10.67,
        "1/1.57 inch": 10.2,
        "1/1.65 inch": 9.7,
        "1/1.67 inch": 9.6,
        "1/1.7 inch": 9.4,
        "1/1.76 inch": 9.1,
        "1/2 inch": 8.0,
        "1/2.3 inch": 6.17,
        "1/2.5 inch": 5.76,
        "1/2.55 inch": 5.64,
        "1/2.6 inch": 5.54,
        "1/3 inch": 4.8,
        "1/3.2 inch": 4.5,
        "1/3.6 inch": 4.0,
        "1/4 inch": 3.6,
    }

    # Check direct match
    for size_name, diagonal in sensor_diagonals.items():
        if size_name in sensor_size_lower:
            return round(full_frame_diagonal / diagonal, 2)

    # Try to parse 1/X inch format
    match = re.search(r"1/(\d+\.?\d*)", sensor_size_lower)
    if match:
        try:
            denominator = float(match.group(1))
            # Approximate diagonal for 1/X inch sensors
            # Using formula based on typical 4:3 aspect ratio sensors
            diagonal = 16.0 / denominator  # Approximate
            return round(full_frame_diagonal / diagonal, 2)
        except ValueError:
            pass

    return None


def lookup_crop_factor(camera_id: str, make: str, model: str) -> Dict[str, Any]:
    """
    Look up crop factor for a camera, first from local database, then online.

    Args:
        camera_id: Combined camera identifier
        make: Camera make
        model: Camera model

    Returns:
        Dictionary with crop factor information
    """
    result = {
        "make": make,
        "model": model,
        "crop_factor": None,
        "sensor_size": None,
        "source": "unknown",
    }

    # First, check local database with exact match
    if camera_id in KNOWN_CROP_FACTORS:
        info = KNOWN_CROP_FACTORS[camera_id]
        result.update(info)
        result["source"] = "local_database"
        return result

    # Check partial matches in local database
    camera_id_lower = camera_id.lower()
    for known_camera, info in KNOWN_CROP_FACTORS.items():
        known_lower = known_camera.lower()
        if known_lower in camera_id_lower or camera_id_lower in known_lower:
            result.update(info)
            result["source"] = "local_database_partial"
            result["matched_entry"] = known_camera
            return result

    # Try online search
    print(f"  Searching online for: {camera_id}")
    online_result = search_crop_factor_online(camera_id)
    if online_result:
        result.update(online_result)
        return result

    # Try searching with just the model if combined didn't work
    if model and model != camera_id:
        print(f"  Searching online for model: {model}")
        online_result = search_crop_factor_online(model)
        if online_result:
            result.update(online_result)
            return result

    result["source"] = "not_found"
    return result


def scan_folders_for_cameras(folders: List[str]) -> Dict[str, Dict[str, Any]]:
    """
    Scan all folders and extract unique camera information.

    Args:
        folders: List of folder paths to scan

    Returns:
        Dictionary mapping camera identifiers to their information
    """
    cameras: Dict[str, Dict[str, Any]] = {}
    processed_files = 0
    skipped_files = 0

    for folder_path in folders:
        folder = Path(folder_path)
        if not folder.exists():
            print(f"Warning: Folder does not exist: {folder_path}")
            continue

        print(f"\nScanning: {folder_path}")

        # Find all image files recursively
        image_extensions = ["*.jpg", "*.JPG", "*.jpeg", "*.JPEG", "*.png", "*.PNG"]
        image_files: List[Path] = []
        for ext in image_extensions:
            image_files.extend(folder.rglob(ext))

        for image_file in image_files:
            processed_files += 1
            if processed_files % 100 == 0:
                print(f"  Processed {processed_files} files, found {len(cameras)} unique cameras...")

            exif = get_exif_data(image_file)
            if exif is None:
                skipped_files += 1
                continue

            camera_info = extract_camera_info(exif)
            if camera_info is None:
                skipped_files += 1
                continue

            make, model, camera_id = camera_info

            if camera_id not in cameras:
                cameras[camera_id] = {
                    "make": make,
                    "model": model,
                    "photo_count": 1,
                    "sample_files": [str(image_file)],
                    "folders": {str(folder_path)},
                }
            else:
                cameras[camera_id]["photo_count"] += 1
                cameras[camera_id]["folders"].add(str(folder_path))
                if len(cameras[camera_id]["sample_files"]) < 3:
                    cameras[camera_id]["sample_files"].append(str(image_file))

    print(f"\nTotal files processed: {processed_files}")
    print(f"Files without camera info: {skipped_files}")
    print(f"Unique cameras found: {len(cameras)}")

    # Convert sets to lists for YAML serialization
    for camera_id in cameras:
        cameras[camera_id]["folders"] = sorted(list(cameras[camera_id]["folders"]))

    return cameras


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    yaml_path = script_dir / "photo_folders.yaml"
    output_path = script_dir / "camera_crop_factors.yaml"

    # Load folder list from YAML
    print(f"Loading folder list from: {yaml_path}")
    if not yaml_path.exists():
        print(f"Error: {yaml_path} not found!")
        return

    with open(yaml_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    folders = config.get("folders", [])
    if not folders:
        print("No folders specified in photo_folders.yaml")
        return

    print(f"Found {len(folders)} folders to scan")

    # Scan all folders for camera information
    print("\n" + "=" * 70)
    print("PHASE 1: Scanning folders for camera information")
    print("=" * 70)
    cameras = scan_folders_for_cameras(folders)

    if not cameras:
        print("No cameras found in the specified folders.")
        return

    # Look up crop factors for each camera
    print("\n" + "=" * 70)
    print("PHASE 2: Looking up crop factors")
    print("=" * 70)

    camera_data: Dict[str, Dict[str, Any]] = {}

    for camera_id in sorted(cameras.keys()):
        info = cameras[camera_id]
        print(f"\nProcessing: {camera_id}")
        print(f"  Photos: {info['photo_count']}, Folders: {len(info['folders'])}")

        # Look up crop factor
        crop_info = lookup_crop_factor(camera_id, info["make"], info["model"])

        # Combine information
        camera_data[camera_id] = {
            "make": info["make"],
            "model": info["model"],
            "photo_count": info["photo_count"],
            "crop_factor": crop_info.get("crop_factor"),
            "sensor_size": crop_info.get("sensor_size"),
            "source": crop_info.get("source", "unknown"),
            "folders": info["folders"],
        }

        if crop_info.get("matched_entry"):
            camera_data[camera_id]["matched_entry"] = crop_info["matched_entry"]
        if crop_info.get("model"):
            camera_data[camera_id]["friendly_name"] = crop_info["model"]

        # Print result
        if crop_info.get("crop_factor"):
            print(f"  -> Crop factor: {crop_info['crop_factor']}x ({crop_info.get('source', 'unknown')})")
        else:
            print("  -> Crop factor: NOT FOUND")

        # Rate limiting for web searches
        if crop_info.get("source") == "web_search":
            time.sleep(1)  # Be nice to search engines

    # Write results to YAML
    print("\n" + "=" * 70)
    print("PHASE 3: Writing results")
    print("=" * 70)

    # Prepare output structure
    output = {
        "description": "Camera crop factors extracted from photo EXIF data",
        "generated": str(Path(__file__).name),
        "cameras": camera_data,
    }

    # Statistics
    total_cameras = len(camera_data)
    found_count = sum(1 for c in camera_data.values() if c.get("crop_factor"))
    not_found_count = total_cameras - found_count

    output["statistics"] = {
        "total_cameras": total_cameras,
        "crop_factors_found": found_count,
        "crop_factors_not_found": not_found_count,
    }

    # Write to YAML file
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(output, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nResults written to: {output_path}")
    print("\nSummary:")
    print(f"  Total cameras: {total_cameras}")
    print(f"  Crop factors found: {found_count}")
    print(f"  Crop factors not found: {not_found_count}")

    # List cameras without crop factors
    if not_found_count > 0:
        print("\nCameras without crop factors (may need manual lookup):")
        for camera_id, info in camera_data.items():
            if not info.get("crop_factor"):
                print(f"  - {camera_id} ({info['photo_count']} photos)")


if __name__ == "__main__":
    main()
