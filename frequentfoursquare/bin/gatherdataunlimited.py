#!/usr/bin/env python
from urllib2 import urlopen
import json
from datetime import datetime

venues = ['40b3de00f964a52027001fe3',
          '4ad4e8faf964a5209ffc20e3',
          '49c440e4f964a520b4561fe3',
          '40b7d280f964a52089001fe3',
          '414e1d80f964a520f21c1fe3',
          '412bd680f964a520c00c1fe3',
          '43e9eb79f964a520212f1fe3',
          '43df51bdf964a520b72e1fe3',
          '428d2880f964a520aa231fe3',
          '40b13b00f964a520ebf61ee3',
          '40e89a00f964a520170a1fe3',
          '40b13b00f964a520e7f61ee3',
          '42911d00f964a520fb231fe3',
          '42a63500f964a5200c251fe3',
          '40b13b00f964a5203bf71ee3',
          '472e59eaf964a520074c1fe3',
          '40b13b00f964a52084f61ee3',
          '43987550f964a520af2b1fe3',
          '46865d5bf964a52040481fe3',
          '44c27b4ff964a520c1351fe3',
          '437e6b00f964a520bd2a1fe3']
time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
url_builder = 'https://api.foursquare.com/v2/venues/{0}/herenow?client_id=MNSGUJNRDL2NU01ELWC4QFE5HOQSC3AI2UMV1PHDL1F2SLOM&client_secret=5AMGF43FMANQSEWQJ124XXWZOXY2RPFGF5BGWJ0F5I2G0PIT'
for venue in venues:
    try:
        url = str.format(url_builder, venue)
        data = urlopen(url).read()
        jsond = json.loads(data)
        # COUNT time venue count
        print str.format('COUNT {0} {1} {2}', time, venue, jsond['response']['hereNow']['count'])
    except:
        pass
