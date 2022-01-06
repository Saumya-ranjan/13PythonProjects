from folium import Map
from geo import Geolocation

latitude = 3.10
longitude = 44.10

location = [latitude, longitude]
mymap = Map( location )
mymap.save("location.html")
mypoint = Geolocation(14.3 , 13.4)
cp = mypoint.closest_parallel()
print(cp)
# print(mymap)