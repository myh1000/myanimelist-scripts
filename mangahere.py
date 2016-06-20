import requests
import re
import codecs
import urllib
import time
import os
import sys
from bs4 import BeautifulSoup
with open('titles.txt', 'r') as file:
    # read a list of lines into data called titles
    titles = file.readlines()
line = 0
auth=('username', 'password')

def post(anime_id):
    xml = """<?xml version="1.0" encoding="UTF-8"?><entry><status>1</status></entry>"""
    address='http://myanimelist.net/api/mangalist/add/'+anime_id+'.xml'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data='data='+xml
    return requests.post(address, data=data, auth=auth, headers=headers).text

def get_titles(filename):
    fi= codecs.open(filename, 'r')
    html = fi.read()
    titles = re.search(b'<dt id="bp.*</dt>', html, flags=re.DOTALL).group(0)
    titles = titles.replace('\n','')
    titles = titles.replace('\t','')
    # print titles
    # links = re.findall(u'<a href="([^"]+)', titles)
    title = []
    soup = BeautifulSoup(titles, 'html.parser')
    for idx, link in enumerate(soup.find_all('a')):
        if (idx % 2 == 0):
            title.append(link.contents[0])
            # print link.contents
    return title

def get_id(name):
    address = 'http://myanimelist.net/api/manga/search.xml?q='+urllib.quote(name)
    print address
    soup = BeautifulSoup(requests.get(address, auth=auth).text, 'xml')
    try:
        return soup.id.contents[0]
    except Exception as error:
        cmd = """open http://myanimelist.net/manga.php?q="""+urllib.quote(name)
        os.system(cmd)
        sys.exit(name + '\n' + repr(error))

def add(name):
    value = post(get_id(name))
    print value
    try:
        int(value)
        titles[line] = "Added: " + titles[line]
    except:
        pass
    with open('titles.txt', 'w') as file:
        file.writelines(titles)

if (len(sys.argv) == 1):
    for title in titles:
        if (title.split(' ', 1)[0] != "Added:" and title.split(' ', 1)[0] != "Skip:"):
            add(title.strip())
            time.sleep(3.5)
        line += 1
else:
    post(get_id(sys.argv[1]))
