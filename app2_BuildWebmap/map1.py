import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
       return 'red'

map = folium.Map(location = [38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="volcanoes")

for lt,ln,el in zip(lat,lon,elev):

    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+"m",
    fill_color=color_producer(el),color='grey',fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Populations")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
