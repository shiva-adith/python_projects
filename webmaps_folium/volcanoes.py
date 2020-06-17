import folium
import pandas
from geopy.geocoders import ArcGIS
from pathlib import Path


nom = ArcGIS()
data = pandas.read_excel("data/Volcano_list_Holocene.xlsx", sheet_name = 0)
latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
elevation = list(data["Elevation"])
mean_elevation = data["Elevation"].mean()
min_elevation = data["Elevation"].min()
max_elevation = data["Elevation"].max()



location = list(nom.geocode("India"))
map = folium.Map(location = location[1], zoom_start = 3, tiles = "Stamen Terrain")

feat_group_underwater = folium.FeatureGroup("Volcanoes Under Water")
feat_group_small = folium.FeatureGroup("Small Volcanoes")
feat_group_large = folium.FeatureGroup("Large Volcanoes")
feat_group_areas = folium.FeatureGroup("Areas")

for lat, long, elev in zip(latitude, longitude, elevation):
    popup = folium.Popup(html=(str(elev)+" m"), min_width = 150)
    if (elev >= min_elevation and elev < 0):
        feat_group_underwater.add_child(folium.CircleMarker(location =[lat,long], radius = 5, popup = popup,
                            fill_color = "blue", color = "grey", fill = True, fill_opacity = 0.5))
    elif 0 < elev <= mean_elevation:
        feat_group_small.add_child(folium.CircleMarker(location =[lat,long], radius = 5, popup = popup,
                            fill_color = "green", color = "grey", fill = True, fill_opacity = 0.5))
    else:
        feat_group_large.add_child(folium.CircleMarker(location =[lat,long], radius = 5, popup = popup,
                            fill_color = "red", color = "grey", fill = True, fill_opacity = 0.5))

feat_group_areas.add_child(folium.GeoJson(data = open("data/world.json", 'r', encoding = 'utf-8-sig').read(),
                            style_function = lambda x: {'fillColor':'white' if x["properties"]["AREA"] < 150000 else "black"},      # try to obtain mean of area instead of trial and error with the cutoff value for fillcolor
                        popup = folium.GeoJsonPopup(fields = ["AREA"], localize=True, labels = True)))

map.add_child(feat_group_underwater)
map.add_child(feat_group_small)
map.add_child(feat_group_large)
map.add_child(feat_group_areas)
map.add_child(folium.LayerControl())
map.save("Volcanoes.html")
