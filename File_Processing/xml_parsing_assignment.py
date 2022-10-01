# Coursera - Python Specialization | Assignment | xml parsing

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
uh = urllib.request.urlopen(url, context=ctx)

total = 0
data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
for i in lst:
    total = total + int(i.find('count').text)

print(total)
