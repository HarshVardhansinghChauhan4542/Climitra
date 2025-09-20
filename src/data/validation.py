import pandas as pd

def validate_coordinates(plants: pd.DataFrame, data_sources: list) -> pd.DataFrame:
    """Check invalid lat/lon values per source."""
    invalid_coords = pd.DataFrame()

    for source in data_sources:
        mask = plants["source_type"] == source

        if source in ["Steel Plants", "Steel Plants with BF"]:
            lat = pd.to_numeric(plants.get("latitude", pd.Series(dtype=float)), errors="coerce")
            lon = pd.to_numeric(plants.get("longitude", pd.Series(dtype=float)), errors="coerce")
            invalid_coords = pd.concat([invalid_coords, plants[mask & ((lat.abs() > 90) | (lon.abs() > 180))]])

        elif source == "Rice Mills":
            lat = pd.to_numeric(plants.get("lat", pd.Series(dtype=float)), errors="coerce")
            lng = pd.to_numeric(plants.get("lng", pd.Series(dtype=float)), errors="coerce")
            invalid_coords = pd.concat([invalid_coords, plants[mask & ((lat.abs() > 90) | (lng.abs() > 180))]])

        elif source == "Geocoded Companies":
            lat = pd.to_numeric(plants.get("Latitude", pd.Series(dtype=float)), errors="coerce")
            lon = pd.to_numeric(plants.get("Longitude", pd.Series(dtype=float)), errors="coerce")
            invalid_coords = pd.concat([invalid_coords, plants[mask & ((lat.abs() > 90) | (lon.abs() > 180))]])

    return invalid_coords
