import urllib.request
from bs4 import BeautifulSoup



url = input('Enter your website')
fhand = urllib.request.urlopen(url)
soup = BeautifulSoup(fhand, 'html.parser')
print(soup)

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))