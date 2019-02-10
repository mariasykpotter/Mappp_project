import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from folium.features import DivIcon

m = folium.Map()
f = open("locations.list", "r")
data = f.readlines()
year_input = input()
map_color = input()
films = []
years = []
tooltip = "♡Click here to see a film♡"

geolocator = Nominatim(
    user_agent="Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

location_layer = folium.FeatureGroup(name='locations')
name_layer = folium.FeatureGroup(name='name')
for el in data:
    if year_input in el:
        i = el.index("(")
        j = el.index(")")
        i1 = el.find("{")
        j1 = el.find("}")
        el = el.replace(el[i1:(j1 + 1)], "")
        years.append(el[(i + 1):j])
        location = el[(j + 1):].replace("\n", "").replace("\t", "")
        lst_location = location.split(",")
        a = lst_location[-1]
        i2 = a.find("(")
        j2 = a.find(")")
        a = a.replace(a[i2:(j2 + 1)], "")
        lst_location.pop()
        lst_location.append(a)
        name = el[:(i - 1)]
        year = el[(i + 1):j]
        if year != year_input or (name, year, location) in films:
            continue
        films.append((name, year, location))
        coordinates = geocode(lst_location[0])
        print(lst_location)
        if not coordinates:
            if len(lst_location) > 1:
                coordinates = geocode(lst_location[1])
        if coordinates:
            print((coordinates.latitude, coordinates.longitude))
            location_layer.add_child(folium.Marker(location=[coordinates.latitude, coordinates.longitude], popup=name,
                                                   icon=folium.Icon(icon="leaf", color=map_color), tooltip=tooltip))
            name_layer.add_child(folium.Marker([coordinates.latitude, coordinates.longitude],
                                               icon=DivIcon(icon_size=(150, 36), icon_anchor=(0, 0),
                                                            html='<div style="font-size: 24pt">{}</div>'.format(
                                                                name), )))

m.add_child(location_layer)
m.add_child(name_layer)

folium.LayerControl().add_to(m)
m.save('Map.html')