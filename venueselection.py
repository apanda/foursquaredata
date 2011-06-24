#!/usr/bin/env python
from geopy import geocoders
from urllib2 import urlopen
import simplejson as json

addresses = ["309 Northeast 45th Street, Seattle, WA", "1928 North 45th Street, Seattle, WA",  "1635 East Olive Way, Seattle, WA", "1001 East Pike Street, Seattle, WA", "1600 Melrose Avenue, Seattle, WA", "332 15th Avenue East, Seattle, WA"]
locations = []

google = geocoders.Google('ABQIAAAAQGbzqUyUyFqkuiq-bCdE0xS4Is1OHekFoVwasBc-LoBG9zsjaBRfMrSYNWNPFnfGOUgXZUAcFXEGrw')
yahoo = geocoders.Yahoo('9E7nLOPV34HwxYM0gRxwbasTCb2juFN1IZJh7N8Zz0xJ.RtlGkdwrD.hJ9li.0vjiGGwR234KA--')

for address in addresses:
    try:
        place, (lat, lng) = google.geocode(address)
        locations.append((lat, lng))
        print str.format("Place: {0}, lat: {1} long: {2}", place, lat, lng)
    except:
        print "ERROR"
url_builder = 'https://api.foursquare.com/v2/venues/search?ll={0},{1}&query=bar&client_id=MNSGUJNRDL2NU01ELWC4QFE5HOQSC3AI2UMV1PHDL1F2SLOM&client_secret=5AMGF43FMANQSEWQJ124XXWZOXY2RPFGF5BGWJ0F5I2G0PIT'
locationdict = {}
for location in locations:
    url = str.format(url_builder, location[0], location[1])
    data = urlopen(url).read()
    jsond = json.loads(data)
    interesting = jsond['response']['groups']
    for group in interesting:
        for item in group['items']:
            locationdict[item['id']] = unicode.format(u'{0} {1} {2} {3}', item['id'], item['name'], item['location']['lat'], item['location']['lng'])

print len(locationdict)

for k, v in locationdict.items():
    print v.encode("iso-8859-1")

