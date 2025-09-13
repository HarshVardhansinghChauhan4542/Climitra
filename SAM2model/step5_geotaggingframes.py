import cv2
import numpy as np
import rasterio
from rasterio.control import GroundControlPoint
from rasterio.transform import from_gcps
import os

# Load the quantized image
img_path = 'ADD HERE.png'
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError("Image not found.")

# 📍 50 GCPs: (x, y) image points ↔ (lon, lat) real-world points
image_points = [[139,320],#gujrat
                [280,25],#jk
                [331,648],#tn
                [704,279]

]

world_coords = [[68.558923,23.547662],
                [74.980897,37.011148],
                [77.507852,8.120545],
                [94.593023,25.317722]

]

# 🧠 Create Ground Control Points
gcps = [
    GroundControlPoint(row=y, col=x, x=lon, y=lat)
    for (x, y), (lon, lat) in zip(image_points, world_coords)
]

# Compute transformation
transform = from_gcps(gcps)

# 💾 Save as GeoTIFF
output_path = 'output/georeferenced_quantized_sugarcane.tif'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with rasterio.open(
    output_path,
    'w',
    driver='GTiff',
    height=img.shape[0],
    width=img.shape[1],
    count=3,
    dtype=img.dtype,
    crs='EPSG:4326',
    transform=transform
) as dst:
    dst.write(img[:, :, 0], 1)
    dst.write(img[:, :, 1], 2)
    dst.write(img[:, :, 2], 3)

print(f"✅ GeoTIFF created: {output_path}")
