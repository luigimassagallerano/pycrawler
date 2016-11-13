from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

url = "http://www-rohan.sdsu.edu/~gawron/index.html"

while url is not None:
    print(url)

    try:
        html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.findAll('a', attrs={'href': re.compile("^http://")})
        tag = random.choice(links)
        link = tag.get('href', None)
        url = link
    except Exception:
        url = random.choice(links).get('href', None)

