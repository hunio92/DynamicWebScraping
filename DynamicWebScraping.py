# pip install -U selenium -> install selenium
# https://github.com/mozilla/geckodriver/releases/download/v0.22.0/geckodriver-v0.22.0-linux32.tar.gz -> webdriver linux
# https://download.mozilla.org/?product=firefox-latest-ssl&os=linux&lang=en-GB -> firefox 32bit

from selenium import webdriver
from bs4 import BeautifulSoup
from store import Db
import time, sys, os, sqlite3
from datetime import datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import WebDriverException


def log(e):
    with open("err.log", "a") as f:
        f.write(str(datetime.now()))
        f.write("  -  ")
        f.write(str(e))
        f.write("\n")
 
# Set headless firefox
os.environ['MOZ_HEADLESS'] = '1'
profile = webdriver.FirefoxProfile()
options = Options()
options.profile = profile
binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_binary=binary, options=options)

# Create database
DATABASE_FILE = 'database.db'
database = Db(DATABASE_FILE)

while(True):
    # Get page content
    try:
        driver.get("http://www.retroradio.hu/")
    except WebDriverException as e:
        log(e)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features="html.parser")

    # Search for title and artist
    artist = soup.find("span", {"class": "js-radio-player-current-artist"})
    title = soup.find("span", {"class": "js-radio-player-current-title"})

    try:
        # Open database
        database.openDB(DATABASE_FILE)

        # Add song to database
        database.addSong(artist.text, title.text)

        # Close database
        database.closeDB()
    except sqlite3.Error as e:
        log(e)

    # Sleep 100s and get new content after
    time.sleep(100)
