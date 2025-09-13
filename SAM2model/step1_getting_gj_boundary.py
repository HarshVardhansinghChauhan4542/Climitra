import geopandas as gpd
import matplotlib.pyplot as plt

# Load full India states shapefile
india_states = gpd.read_file("gadm41_IND_1.shp")

# Filter for Gujarat
gujarat_boundary = india_states[india_states['NAME_1'] == 'Gujarat']

# Save Gujarat-only shapefile (optional)
gujarat_boundary.to_file("gujarat_boundary.shp")

#visualize
gujarat_boundary.plot(edgecolor='black', facecolor='none')
plt.title("Gujarat State Boundary")
plt.show()