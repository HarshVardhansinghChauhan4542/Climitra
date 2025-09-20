import json
import os

def load_geojson_chunked(filename, max_features=5000):
    """Load large GeoJSON with feature limit to avoid memory issues."""
    if not os.path.exists(filename):
        return None, False

    with open(filename, "r") as f:
        data = json.load(f)

    if len(data.get("features", [])) > max_features:
        return {"type": "FeatureCollection", "features": data["features"][:max_features]}, True
    return data, False


def generate_hover_texts(df, source, hover_name_col):
    """Generate hover texts for plant/company datasets."""
    hover_texts = []
    for _, row in df.iterrows():
        name = row.get(hover_name_col, "Unknown")
        text = f"<b>{source}</b><br>{hover_name_col}: {name}"
        hover_texts.append(text)
    return hover_texts
