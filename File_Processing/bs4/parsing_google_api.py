# Practice Purpose
# Fetching the geo location( lat, long ) from the google api by sending few letters of the concerned address
# Right now google api is not free, hence we could not confirm the program's success
# But logic is same how to retrieve, parse and send the address details from
# google api to the user

import urllib.request
import urllib.parse
import urllib.error
import json

# Note that google is needing key for this url
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter the required location : ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    received_data = urllib.request.urlopen(url)
    data = received_data.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('----Failure in receiving the details----')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    long = js["results"][0]["geometry"]["location"]["lng"]
    print('Latitude : ', lat)
    print('Longitude : ', long)
    location = js["results"][0]["formatted_address"]
    print(location)
