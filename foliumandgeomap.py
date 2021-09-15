import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import folium
import webbrowser

# define the world map
world_map = folium.Map()

# different type of maps
# world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')
# world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Terrain')

# get data
df_incidents = pd.read_csv('source/Police_Department_Incidents_-_Previous_Year__2016_.csv')
print(df_incidents.head())

# get the first 100 crimes in the df_incidents dataframe
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

from folium import plugins

# let's start again with a clean copy of the map of San Francisco
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# instantiate a mark cluster object for the incidents in the dataframe
incidents = plugins.MarkerCluster().add_to(sanfran_map)

# loop through the dataframe and add each data point to the mark cluster
for lat, lng, label, in zip(df_incidents.Y, df_incidents.X, df_incidents.Category):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(incidents)


# display map
def show_map(map):
    map.save('map.html')
    webbrowser.open('map.html')


show_map(sanfran_map)

# Choropleth
