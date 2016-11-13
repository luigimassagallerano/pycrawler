import urllib2
import re
from bs4 import BeautifulSoup

url = "http://www-rohan.sdsu.edu/~gawron/index.html"

html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
links = soup.findAll('a', attrs={'href': re.compile("^http://")})

for tag in links:
    link = tag.get('href', None)
    if link is not None and link:
        print link
