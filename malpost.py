#!/usr/bin/python
import sys
import urllib
import os
from bs4 import BeautifulSoup
import requests
username = 'username'
auth=(username, 'password')

def get_id(name):
    address = 'http://myanimelist.net/api/anime/search.xml?q='+urllib.quote(name)
    soup = BeautifulSoup(requests.get(address, auth=auth).text, 'xml')
    try:
        return soup.id.contents[0]
    except Exception as error:
        cmd = """osascript /Applications/VLC.app/Contents/MacOS/share/lua/extensions/chrome.applescript http://myanimelist.net/anime.php?q="""+urllib.quote(name)
        os.system(cmd)
        sys.exit(name + '\n' + repr(error))

def anime_list():
    address = 'http://myanimelist.net/malappinfo.php?u='+username.strip("\s+")+'&status=all&type=anime'
    data = requests.get(address).text
    anime = []
    soup = BeautifulSoup(data, 'xml')
    for tag in soup.find_all('series_animedb_id'):
        anime.append(tag.contents[0])
    return anime

def post(title):
    anime_id = get_id(title)
    anime = anime_list()
    if anime_id in anime:
        print update(anime_id, "301")
    else:
        print add(anime_id)

def add(anime_id):
    xml = """<?xml version="1.0" encoding="UTF-8"?><entry><status>1</status></entry>"""
    address='http://myanimelist.net/api/animelist/add/'+anime_id+'.xml'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data='data='+xml
    return requests.post(address, data=data, auth=auth, headers=headers).text

def update(anime_id, ep_count):
    xml = """<?xml version="1.0" encoding="UTF-8"?><entry><episode>"""+ep_count+"""</episode><status>1</status></entry>"""
    address='http://myanimelist.net/api/animelist/update/'+anime_id+'.xml'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data='data='+xml
    return requests.post(address, data=data, auth=auth, headers=headers).text

if (len(sys.argv) != 2):
    sys.exit("Error: Please format like 'malpost.py title'")
else:
    post(sys.argv[1])
