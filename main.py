import requests
from bs4 import BeautifulSoup as bsoup
import random

# used for css retrieve
from urllib.parse import urljoin

# this make prettify working
import collections
collections.Callable = collections.abc.Callable

# URL to scrap
url = "https://docs.python.org/3/"

# initialize session
session = requests.Session()

# get html code
html = session.get(url).content

# parse html content
soup = bsoup(html, "html.parser")
html_soup = soup.prettify()

# create html file
rdm = random.randrange(0,1000)
with open(f'index{rdm}.html', 'w') as html:
    html.write(html_soup)

# get css list of links
css_files = []

for css in soup.find_all("link"):
    if css.attrs.get("href"):
        # if the link tag has the 'href' attribute
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)

with open("css_files.txt", "w") as f:
    for css_file in css_files:
        print(css_file, file=f)
