import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import collections

# Ignoring the SSL certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

collections.Callable = collections.abc.Callable

#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' 1st testing url
#url = 'http://py4e-data.dr-chuck.net/known_by_Zayne.html' 1st testing url
url = input("Enter url: ")
count = input("Enter count: ")
position = input("Enter position: ")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')
i = 1

while i<=int(count):
    tags = soup('a')
    print(tags[int(position)-1].get('href'))
    tags = urllib.request.urlopen(tags[int(position)-1].get('href'), context = ctx).read()
    soup = BeautifulSoup(tags, 'html.parser')
    i = i+1
