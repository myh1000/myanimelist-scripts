import codecs
from bs4 import BeautifulSoup
import re
for x in range(1, 10): # change these to the number of bookmarked pages
    f = codecs.open(str(x)+".html", 'r')
    html = f.read()
    titles = re.search(b'<dt id="bp.*</dt>', html, flags=re.DOTALL).group(0)
    titles = titles.replace('\n','')
    titles = titles.replace('\t','')
    soup = BeautifulSoup(titles, 'html.parser')
    f = open('titles.txt', 'a')
    for idx, link in enumerate(soup.find_all('a')):
        if (idx % 2 == 0):
            f.write(link.contents[0])
            f.write("\n")
    f.close()
