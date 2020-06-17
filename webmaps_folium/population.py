import folium
import pandas
from geopy.geocoders import ArcGIS
from pathlib import Path



loc_obj = ArcGIS()
base_loc = list(loc_obj.geocode("India"))
map = folium.Map(location= base_loc[1], zoom_start = 5, tiles= 'OpenStreetMap')

data = pandas.read_csv("data/pop2020.csv")

current_pop = list(data["Population"])
countries_list = list(data["Country"])
latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
density = list(data["Density"])

feat_group_north = folium.FeatureGroup("Northern Hemisphere")
feat_group_south = folium.FeatureGroup("Southern Hemisphere")
feat_group_polygons = folium.FeatureGroup("Shape")

for lat,lon,country,population in zip(latitude,longitude, countries_list,current_pop):
    # pop_str = "{:,}".format(population)
    popup_str = "{} : {:,}".format(country, population)
    if lat >= 0:
        feat_group_north.add_child(folium.CircleMarker(location =[lat,lon], radius=5, popup=popup_str,
                                   fill_color='red', color='black', fill_opacity=0.5))
    else:
        feat_group_south.add_child(folium.CircleMarker(location=[lat,lon], radius=5, popup=popup_str,
                                   fill_color='green', color='grey', fill_opacity=0.5))

# data_folder = Path('F:/College/Programming/Python/Udemy course/2-Webmaps')
# file_path = data_folder / "world.json"

# for den in density:
#     style_func = lambda x : {'fillColor': 'darkgreen' if\
#                              den <=100 else 'lightgreen' if\
#                              100 < den <=500 else 'orange' if\
#                              500 < den <= 1000 else 'red'}


# feat_group_polygons.add_child(folium.GeoJson(data = open(file_path, 'r', encoding='utf-8-sig').read(),
#                               style_function = lambda x : {'fillColor': 'darkgreen' if\
#                                                        den <=100 else 'lightgreen' if\
#                                                        100 < den <=500 else 'orange' if\
#                                                        500 < den <= 1000 else 'red'},
#                                ))
#break polygon and style func into diff var and try it out

map.add_child(feat_group_south)
map.add_child(feat_group_north)
map.add_child(folium.LayerControl())
map.save("Population.html")

# for country in countries_list:
#     location_list = list(loc_obj.geocode(country))

# c= input("Enter country: ")
# if c in location_list:
#     print(c)
