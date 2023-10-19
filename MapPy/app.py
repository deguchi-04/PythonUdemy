import folium
import pandas as pd

def color(elev):
    if elev <= 2000:
        color = "blue"
    elif 2000 < elev <= 3000:
        color = "green"
    elif elev > 3000:
        color = "red"
    return color

def main():
    df = pd.read_csv("MapPy/Volcanoes.txt")
    lat = list(df["LAT"])
    lon = list(df["LON"])
    elev = list(df["ELEV"])

    map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
    fgv = folium.FeatureGroup(name="Volcanoes")
    fgp = folium.FeatureGroup(name="Population")
    for coordinatesLat, coordinatesLon, elevation in zip(lat,lon,elev):
        fgv.add_child(folium.CircleMarker(location=[coordinatesLat,coordinatesLon],radius=6, popup=folium.Popup(str(elevation)+" m", parse_html=True), fill_color=color(elevation), color=color(elevation), fill_opacity=0.7))

    fgp.add_child(folium.GeoJson(data=open("MapPy/world.json", "r", encoding='utf-8-sig').read(), 
                                style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    
    map.add_child(fgp)
    map.add_child(fgv)
    map.add_child(folium.LayerControl())
    map.save("MapPy/Map1.html")

if __name__ == '__main__':
    main()