import rasterio
from rasterio.mask import mask
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

# Load Gujarat boundary shapefile
gujarat_boundary = gpd.read_file("gujarat_boundary.shp")
gujarat_boundary = gujarat_boundary.to_crs("EPSG:4326")  # match CRS with raster

# Load merged ESA raster
esa_raster = rasterio.open("gujarat_esa_merged.tif")

# Mask ESA raster to Gujarat boundary
geoms = gujarat_boundary.geometry.values
esa_clip, transform = mask(esa_raster, geoms, crop=True)
esa_clip = esa_clip[0]  # single band

# Create grassland-shrubland mask
# ESA Class codes: 20 = Grassland, 30 = Shrubland
mask_grass_shrub = np.isin(esa_clip, [20, 30])

out_meta = esa_raster.meta.copy()
out_meta.update({
    "driver": "GTiff",
    "height": mask_grass_shrub.shape[0],
    "width": mask_grass_shrub.shape[1],
    "transform": transform,
    "count": 1,
    "dtype": rasterio.uint8,
    "crs": esa_raster.crs
})

with rasterio.open("grassland_shrubland_mask.tif", "w", **out_meta) as dst:
    dst.write(mask_grass_shrub.astype(rasterio.uint8), 1)


# # Optional: Visualize
# plt.imshow(mask_grass_shrub, cmap='Greens')
# plt.title("Grassland + Shrubland Mask")
# plt.axis("off")
# plt.show()
