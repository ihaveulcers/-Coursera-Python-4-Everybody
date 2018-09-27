import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#url = ('http://py4e-data.dr-chuck.net/comments_138833.xml')
url = input('Enter location:')
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
# find all <comment> within  <comments> , data structure = list []
list = tree.findall('comments/comment')

count = 0
sum = 0

for item in list:
    commentcount = int(item.find('count').text)
    count = count + 1
    sum = sum + commentcount

print ('Count:',count)
print ('Sum:',sum)
