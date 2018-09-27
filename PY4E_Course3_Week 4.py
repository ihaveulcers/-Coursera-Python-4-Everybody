###########################################################################
##################### COURSE 3 WEEK 4 ASSIGNMENT 1 ########################
###########################################################################

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('enter url to scrape -')  # http://py4e-data.dr-chuck.net/comments_138831.html
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup (html,'html.parser')

spancounts = 0
sum = 0

x = soup('span')
for span in x:
    sum += int(span.contents[0])
    spancounts += 1

print('count ',spancounts)    #print 50
print('sum ',sum)             #print 2553


###########################################################################
##################### COURSE 3 WEEK 4 ASSIGNMENT 2 ########################
###########################################################################

import urllib.request
from bs4 import BeautifulSoup

#url = ('http://py4e-data.dr-chuck.net/known_by_Blair.html')

url = input('Enter URL:')
position = int(input('Enter position:'))     # position = 18
count = int(input('Enter count:'))      # count = 7

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    tags = soup('a')
    s = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)

    print (s[position-1])
    url = s[position-1]
