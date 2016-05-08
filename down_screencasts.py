#!/usr/bin/env python3
# down_screencasts.py - downloads all the vim screencasts on vimcasts.org
from bs4 import BeautifulSoup
import requests
import urllib.request
from os.path import basename

########## BEGIN CONFiG

url = 'http://media.vimcasts.org/videos/{}' # Url of the video's on vimcasts.org
ext = 'm4v' # The type of extension you want
download_folder = '/home/nico/Video\'s/vimcasts/' # Folder you want to download into
n_vimcasts = 69 # Number of current vimcasts

########## END CONFIG

def ls(url, ext):
    """ Returns a list of url's having the given extension

    :param url: the url of which you want the url's
    :param ext: the extension of the files you want
    """
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for i in range(1,n_vimcasts):
    for f in ls(url.format(i), ext):
        print(f)
        urllib.request.urlretrieve(f,
               download_folder  + str(i) + '_' + basename(f))
