from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


cobalt_map = Basemap(llcrnrlon=-117.3, llcrnrlat=41.9, urcrnrlon=-111.0, urcrnrlat=49.0, projection='lcc', lat_1=43, lat_2=45, lon_0=-114)
cobalt_map.drawstates(color='b')
cobalt_map.drawmapboundary()
cobalt_map.drawcounties(color='darkred')
cobalt_lon, cobalt_lat = cobalt_map(-114.625, 44.75)
cobalt_map.plot(cobalt_lon, cobalt_lat, 'bo', markersize=8)

plt.title('Cobalt Map', fontsize=10)
plt.show()


