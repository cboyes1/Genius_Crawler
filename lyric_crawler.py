import os
import time
import requests
from bs4 import BeautifulSoup
import mechanicalsoup



#File Path of Script
HERE = os.path.dirname(os.path.abspath(__file__))


#try making a new text file to store lyrics
try:
    with open(os.path.join(HERE, 'test_lyric.txt'), 'x') as file:
        pass

except FileExistsError:
    pass


browser = mechanicalsoup.StatefulBrowser()
browser.open("https://genius.com/Bing-crosby-i-cant-begin-to-tell-you-lyrics")
browser.get_current_page().find_all('p')

print(browser.get_current_page().find_all('p'))

LINES = []

for p in browser.get_current_page().find_all("p"):
    LINES.append(p.text)

with open(os.path.join(HERE, 'test_lyric.txt'), 'w') as file:
    for line in LINES:
            file.write(line)

        