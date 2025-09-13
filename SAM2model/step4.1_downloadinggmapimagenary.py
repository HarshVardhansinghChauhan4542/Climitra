import os
import time
import folium
import geopandas as gpd
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from shapely.geometry import Point
from tqdm import tqdm

# === CONFIG ===
ZOOM_LEVEL = 18
TILE_FOLDER = "tiles"
MAX_WORKERS = 20  # Adjust based on available memory (12.8GB)
os.makedirs(TILE_FOLDER, exist_ok=True)

# === LOAD GRID ===
fishnet = gpd.read_file("gujarat_fishnet_1km_optimized.shp")
fishnet = fishnet.to_crs(epsg=4326)

# === GENERATE TASK LIST ===
tile_tasks = []
for i, row in fishnet.iterrows():
    center = row.geometry.centroid
    tile_tasks.append((i, center.y, center.x))  # (tile_id, lat, lon)

# === FUNCTION TO DOWNLOAD ONE TILE ===
def download_tile(task):
    i, lat, lon = task
    out_path = os.path.join(TILE_FOLDER, f"tile_{i}.png")

    # Skip if already exists
    if os.path.exists(out_path):
        return f"[{i}] Already exists, skipped"

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=512,512")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        m = folium.Map(
            location=[lat, lon],
            zoom_start=ZOOM_LEVEL,
            tiles=None,
            control_scale=True,
        )
        folium.TileLayer(
            tiles="http://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
            attr="Google",
            name="Google Satellite",
            overlay=False,
            control=True,
        ).add_to(m)

        map_file = f"temp_map_{i}.html"
        m.save(map_file)

        driver.get("file://" + os.path.abspath(map_file))
        time.sleep(2.5)
        driver.save_screenshot(out_path)

        driver.quit()
        os.remove(map_file)

        return f"[{i}] Saved: {out_path}"
    except Exception as e:
        return f"[{i}] Error: {e}"

# === PARALLEL DOWNLOAD ===
if __name__ == "__main__":
    print(f"Total tiles to download: {len(tile_tasks)}")
    with Pool(processes=MAX_WORKERS) as pool:
        for result in tqdm(pool.imap_unordered(download_tile, tile_tasks), total=len(tile_tasks)):
            print(result)
