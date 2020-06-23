import folium
import pandas

# Create map object
map = folium.Map(
    location=[0.0, 0.0],
    zoom_start=6,
    tiles='Stamen Terrain'
)

fg = folium.FeatureGroup(name="Volcanoes")

data = pandas.read_csv("volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
names = list(data['NAME'])
statuses = list(data['STATUS'])
types = list(data['TYPE'])


def render(name, height, status, typ):
    return folium.IFrame(
        html=f"""
<h4>Volcano info:</h4>
<ul>
<li>Name: {name}</li>
<li>Height: {height}</li>
<li>Status: {status}</li>
<li>Type: {typ}</li>
</ul>""",
        width=250,
        height=150
    )


def color(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 2000:
        return 'orange'
    elif 2000 <= elev < 3000:
        return 'purple'
    elif 3000 <= elev < 4000:
        return 'red'
    else:
        return 'darkred'


for lt, ln, el, na, st, ty in zip(lat, lon, elev, names, statuses, types):
    iframe = render(na, el, st, ty)
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            icon=folium.Icon(color=color(el))
        )
    )

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open(
            'world.json',
            'r',
            encoding='utf-8-sig'
        ).read(),
        style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}
    )
)

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('volcanoes.html')
