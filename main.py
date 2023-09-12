import geopy
​
API_KEY = ""

geolocator = geopy.geocoders.Bing(API_KEY)
​
def address_to_coordinates(address):
    location = geolocator.geocode(address)
    if hasattr(location, 'latitude') and hasattr(location, 'longitude'):
        return (location.latitude, location.longitude)
    else:
        return None
​
addresses = ["Parco Ducale, Parma, Italy"] #List of addresses to convert
coordinates = [] #List of coordinates results

for address in addresses:
    coordinate = address_to_coordinates(address)
    coordinates.append(coordinate)
    
print(coordinates)



