from multiprocessing.connection import Client
from bs4 import BeautifulSoup
import requests
# from PyQt4.QtGui import QApplication
# from PyQt4.QtCore import QUrl
# from PyQt4.QtWebKit import QWebPage
import re
import sys
import os
import json
# from selenium import webdriver
#from requests_html import HTMLSession


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



DATA_IN_JSON = 'publications.json'
out_json = {}


if __name__ == '__main__':

    driver = webdriver.Chrome(ChromeDriverManager().install())

    # driver = webdriver.PhantomJS()
    # Get the publications
    with open(DATA_IN_JSON, 'r') as f:
        publications = json.load(f)
    i = 0
    for author in publications:
        if author not in ['xiaowei zhuang', 'long cai']:
            out_json[author] = {}
            for pub in publications[author]:

                if pub['bib']['title'] != 'Turning single cells into microarrays by super-resolution barcoding':
                    print("Getting text for: " + pub['bib']['title'])
                    url = pub['pub_url']
                    driver.get(url)
                    html = driver.page_source
                    soup = BeautifulSoup(html)
                    out_json[author][pub['bib']['title']] = soup.get_text()
                    # print(out_json[author][pub['bib']['title']])
                    if i % 30 == 0:
                        with open(f'publications_text_{i}.json', 'w') as f:
                            json.dump(out_json, f, indent=4)
                i += 1

    with open(f'publications_text_{i}.json', 'w') as f:
        json.dump(out_json, f, indent=4)

    driver.close()