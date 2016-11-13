import urllib2
import re
import random
from bs4 import BeautifulSoup

url = "http://www-rohan.sdsu.edu/~gawron/index.html"

while url is not None:
    print url

    try:
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        links = soup.findAll('a', attrs={'href': re.compile("^http://")})
        tag = random.choice(links)
        link = tag.get('href', None)
        url = link
    except Exception:
        url = random.choice(links).get('href', None)

