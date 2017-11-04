import folium
import pandas

map = folium.Map(location=[1.3143394,103.7041608], zoom_start=12, tiles="Mapbox Bright")
fg_volcano = folium.FeatureGroup(name="Volcanoes")

data = pandas.read_csv("Volcanoes_USA.txt")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]

def color_producer(elevation):
    if elevation < 2000:
        return "green"
    else:
        return "red"


for i, k, j in zip(lat, lon, elev):
    # fg.add_child(folium.Marker(location=[i,k], popup=str(j) + " m", icon=folium.Icon(color=color_producer(j), icon_color="blue")))
    fg_volcano.add_child(folium.CircleMarker(location=[i,k], popup=str(j) + " M", color=color_producer(j), fill=True, fill_color=color_producer(j), fill_opacity=0.8))

fg_population = folium.FeatureGroup(name="Population")
world_data = open("world.json", "r", encoding="utf-8-sig")
fg_population.add_child(folium.GeoJson(data=world_data.read(),
                            style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"] < 10000000
                            else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"})) # if no encoding, will get an error telling you the encoding needed (utf-8-sig)

map.add_child(fg_volcano)
map.add_child(fg_population) # keep code more organised using FeatureGroup and for layer control to be separated for each featuregroup
                                # if we do not use featuregroup and add features to the map directly, when we implment layercontrol,
                                # there will be a control for every since volcano because we add_child for each one
map.add_child(folium.LayerControl()) # must be placed after add_child method so that the controls can be create for all child in the map object

map.save("Map1.html")