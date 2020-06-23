import folium


# Create map object
map = folium.Map(
    location=[38.58, -99.09],
    zoom_start=6,
    tiles='Stamen Terrain'
)

fg = folium.FeatureGroup(name="My Group")
# Add markers
fg.add_child(
    folium.Marker(
        location=[38.2, -99.1],
        popup='Hello Map',
        icon=folium.Icon(color='green')
    )
)

map.add_child(fg)

map.save('Map1.html')
