import urllib.request
from bs4 import BeautifulSoup



url = input('Enter your website')
fhand = urllib.request.urlopen(url)
soup = BeautifulSoup(fhand, 'html')
for line in fhand:
    print(line.decode().strip())

