import os
from bs4 import BeautifulSoup
# Python 3.x
from urllib.request import urlopen, urlretrieve
import re

URL = 'https://solidarites-sante.gouv.fr/systeme-de-sante-et-medico-social/innovation-et-recherche/l-innovation-et-la-recherche-clinique/appels-a-projets/article/les-projets-retenus'
URL2 = 'https://solidarites-sante.gouv.fr'
OUTPUT_DIR = './data'  # path to output folder, '.' or '' uses current folder

u = urlopen(URL)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, "lxml")




for link in soup.findAll('a', attrs={'href': re.compile(r'.xls|.xlsx$')}):
    href = f'{URL2}/{link.get("href")}'
    print(href)


# for link in soup.select('a[href^="http://"]'):
#     href = link.get('href')
#     if not any(href.endswith(x) for x in ['.csv', '.xls', '.xlsx']):
#         continue


    filename = os.path.join(OUTPUT_DIR, href.rsplit('/', 1)[-1])

    # We need a https:// URL for this site
    href = href.replace('http://', 'https://')

    print("Downloading %s to %s..." % (href, filename) )
    urlretrieve(href, filename)
    print("Done.")

print (href)