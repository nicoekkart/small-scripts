#!/usr/bin/env python3
# xkcd_downloader.py - Downloads all xkcd comics.

import requests
import os
import bs4

url = 'http://www.xkcd.com'  # Starting url
# Create directory for comics
folderUrl = '/home/nico/Afbeeldingen/xkcd'
os.makedirs(folderUrl, exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(
                os.path.join(folderUrl, os.path.basename(comicUrl)), 'wb')
            for chunck in res.iter_content(100000):
                imageFile.write(chunck)
            imageFile.close()
            # Get the Prev button's url.
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
        except:
            # Skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

print('Done!')
