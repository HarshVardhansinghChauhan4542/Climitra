import json
import os

def load_geojson_metadata(path="assets/metadata/geojson_metadata.json"):
    """Load GeoJSON metadata from a JSON file."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Metadata file not found: {path}")
    with open(path, "r") as f:
        return json.load(f)
