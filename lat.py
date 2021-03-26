from geopy.geocoders import Nominatim
from geopy.point import Point
import geopy
import csv

geopy.geocoders.options.default_user_agent = "my-app"



address = []
longlat=[]

with open('longlat.csv',newline='',encoding='utf-8-sig') as csvfile:
    reading = csv.reader(csvfile)
    for row in reading:
        longlat.append(row)

    
    
  
for location in longlat:
    for x in location:
        
        location_string = x.split(',')
        lat = float(location_string[0])
        longg = float(location_string[-1]) 

        geolocator = Nominatim()
        full_address = geolocator.reverse("{}, {}".format(lat, longg))

        address.append(full_address.address)
        print(full_address.address) 
    




