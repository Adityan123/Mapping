import folium
import pandas

data = pandas.read_csv('salemplaces.txt')
Lat = list(data['Lat'])
Long = list(data['Long'])
Name = list(data['Name'])
terain = list(data['Terain'])

map = folium.Map(location=[11.66246563568823,
                 78.14172511628485], tiles="Stamen Terrain")

fgc = folium.FeatureGroup(name="Places")


def color_producer(Ter):
    if Ter == "city":
        return 'blue'
    elif Ter == "hills":
        return 'green'
    else:
        return 'red'


for lt, ln, na, tr in zip(Lat, Long, Name, terain):
    fgc.add_child(folium.CircleMarker(location=[lt, ln], popup=na,
                                      fill_color=color_producer(tr), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="World Population")

fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")
