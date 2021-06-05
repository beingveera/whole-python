import folium as fl
from folium import plugins
m=fl.Map(location=[45.372,-121.6972])
fl.Marker([45.372,-121.6972],popup='<i>Mt. Hood Meadows</i>',tooltip='click me').add_to(m)

