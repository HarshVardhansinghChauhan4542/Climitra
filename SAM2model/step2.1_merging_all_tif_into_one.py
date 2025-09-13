import rasterio
from rasterio.merge import merge
import glob

# Change path if needed
esa_files = glob.glob("tif/ESA_WorldCover_10m_2021_v200_N*.tif")

# Open all 6 raster tiles
src_files_to_mosaic = [rasterio.open(f) for f in esa_files]

# Merge
mosaic, out_transform = merge(src_files_to_mosaic)

# Save
out_meta = src_files_to_mosaic[0].meta.copy()
out_meta.update({
    "driver": "GTiff",
    "height": mosaic.shape[1],
    "width": mosaic.shape[2],
    "transform": out_transform,
    "crs": src_files_to_mosaic[0].crs
})

with rasterio.open("gujarat_esa_merged.tif", "w", **out_meta) as dest:
    dest.write(mosaic)
