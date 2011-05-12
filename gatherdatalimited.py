#!/usr/bin/env python
from urllib2 import urlopen
import simplejson as json
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
time = datetime.now().isoformat()
url_builder = 'https://api.foursquare.com/v2/venues/{0}/herenow?oauth_token=NAS0BF2TRCO1L2CAHW3SNYXFAW2W3CIJJ5UYM03EKAS4310C'
for venue in venues:
    url = str.format(url_builder, venue)
    data = urlopen(url).read()
    jsond = json.loads(data)
    print unicode.format(u'COUNT {0} {1} {2}', time, venue, jsond['response']['hereNow']['count']).encode("iso-8859-1")
    for item in jsond['response']['hereNow']['items']:
        user = item['user']
        if not 'firstName' in user:
            user['firstName'] = ""
        if not 'lastName' in user:
            user['lastName'] = ""
        if not 'gender' in user:
            user['gender'] = 'unknown'
        # CHECKIN time venue checkinid createdAt type userid firstname lastname gender
        print unicode.format(u'CHECKIN {0} {1} {2} {3} {4} {5} {6} {7} {8}', time, 
            venue, 
            item['id'], 
            item['createdAt'], 
            item['type'], 
            user['id'], 
            user['firstName'], 
            user['lastName'], 
            user['gender'])
