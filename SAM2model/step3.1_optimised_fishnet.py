import geopandas as gpd
from shapely.geometry import box
import numpy as np
from shapely.ops import unary_union
import time

def create_optimized_fishnet(gdf, grid_size):
    """
    Optimized fishnet creation - trades some precision for massive speed gains
    """
    print("Starting optimized fishnet creation...")
    start_time = time.time()
    
    # Get bounds
    minx, miny, maxx, maxy = gdf.total_bounds
    print(f"Gujarat bounds: {(maxx-minx)/1000:.1f}km x {(maxy-miny)/1000:.1f}km")
    
    # Create Gujarat union for intersection testing (this is the key optimization)
    print("Creating Gujarat boundary union...")
    gdf_union = unary_union(gdf.geometry)
    union_time = time.time()
    print(f"Union created in {union_time - start_time:.1f} seconds")
    
    # Generate coordinate arrays
    x_coords = np.arange(minx, maxx, grid_size)
    y_coords = np.arange(miny, maxy, grid_size)
    
    total_potential = len(x_coords) * len(y_coords)
    print(f"Total potential grid cells: {total_potential:,}")
    
    # Pre-filter cells that intersect Gujarat (MAJOR optimization)
    print("Pre-filtering intersecting cells...")
    intersecting_cells = []
    
    for i, x0 in enumerate(x_coords):
        if i % 50 == 0:  # Progress indicator
            print(f"Progress: {i}/{len(x_coords)} ({i/len(x_coords)*100:.1f}%)")
            
        for y0 in y_coords:
            x1 = x0 + grid_size
            y1 = y0 + grid_size
            cell = box(x0, y0, x1, y1)
            
            # Quick intersection test with union
            if cell.intersects(gdf_union):
                intersecting_cells.append(cell)
    
    filter_time = time.time()
    print(f"Pre-filtering completed in {filter_time - union_time:.1f} seconds")
    print(f"Intersecting cells found: {len(intersecting_cells):,}")
    print(f"Cells eliminated: {total_potential - len(intersecting_cells):,} ({(1-len(intersecting_cells)/total_potential)*100:.1f}%)")
    
    # Create GeoDataFrame with only intersecting cells
    fishnet = gpd.GeoDataFrame({'geometry': intersecting_cells}, crs=gdf.crs)
    gdf_time = time.time()
    print(f"GeoDataFrame created in {gdf_time - filter_time:.1f} seconds")
    
    # Now do precise clipping (much faster with pre-filtered data)
    print("Performing precise clipping...")
    fishnet_clip = gpd.overlay(fishnet, gdf, how='intersection')
    clip_time = time.time()
    print(f"Clipping completed in {clip_time - gdf_time:.1f} seconds")
    
    # Add useful attributes
    fishnet_clip['grid_id'] = range(len(fishnet_clip))
    fishnet_clip['area_sqkm'] = fishnet_clip.geometry.area / 1e6
    
    total_time = time.time() - start_time
    print(f"\nTOTAL TIME: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")
    print(f"Final fishnet: {len(fishnet_clip):,} grid cells")
    
    return fishnet_clip

# Load Gujarat boundary
print("Loading Gujarat boundary...")
gdf = gpd.read_file("gujarat_boundary.shp")
original_crs = gdf.crs
gdf = gdf.to_crs(epsg=32643)  # Project to UTM Zone 43N

# Define grid size
grid_size = 1000  # 1 km

# Create optimized fishnet
fishnet_clip = create_optimized_fishnet(gdf, grid_size)

# Save result
output_file = "gujarat_fishnet_1km_optimized.shp"
fishnet_clip.to_file(output_file)
print(f"\nFishnet saved to: {output_file}")

# Quality check - show some statistics
print(f"\nQUALITY CHECK:")
print(f"- Total cells: {len(fishnet_clip):,}")
print(f"- Average cell area: {fishnet_clip['area_sqkm'].mean():.3f} sq km")
print(f"- Min cell area: {fishnet_clip['area_sqkm'].min():.3f} sq km")
print(f"- Max cell area: {fishnet_clip['area_sqkm'].max():.3f} sq km")
print(f"- Total area covered: {fishnet_clip['area_sqkm'].sum():.1f} sq km")

# Optional: Convert back to original CRS if needed
if original_crs != 'EPSG:32643':
    fishnet_clip_original = fishnet_clip.to_crs(original_crs)
    fishnet_clip_original.to_file("gujarat_fishnet_1km_original_crs.shp")
    print(f"Also saved in original CRS: gujarat_fishnet_1km_original_crs.shp")

print("\nOptimization complete! ✓")