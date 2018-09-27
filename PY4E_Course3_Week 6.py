########################################################################
##################### COURSE 3 WEEK 6 ASSIGNMENT 1 #####################
########################################################################

import urllib.request
import json

#url = ('http://py4e-data.dr-chuck.net/comments_138834.json')
url = input('Enter URL:')

print('Retrieving:',url)
data = urllib.request.urlopen(url).read().decode()
print('Retrievd:',len(data),'characters')

object = json.loads(data)

sum = 0
count = 0

for comment in object['comments']:
    sum += int(comment['count'])
    count += 1

print('count:',count)
print('sum:',sum)


########################################################################
##################### COURSE 3 WEEK 6 ASSIGNMENT 2 #####################
########################################################################

import urllib.request, urllib.parse
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

#address = ('King Mongkuts University of Technology Thonburi')
address = input("Enter location: ")

parameter = {"sensor": "false", "address": address}
url = serviceurl + urllib.parse.urlencode(parameter)
print("Retrieving ", url)

data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

object = json.loads(data)
place_id = object["results"][0]["place_id"]
print("Place id", place_id)
