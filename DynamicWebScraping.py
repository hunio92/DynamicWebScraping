# pip install -U selenium -> install selenium
# https://chromedriver.storage.googleapis.com/index.html?path=2.42/ -> ChromeDriver Win/Linux

from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup  
from store import Db 
import time, sys

# Set headless chrome
chrome_options = Options()    
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu") 
driver = webdriver.Chrome(chrome_options=chrome_options)
# Create database
DATABASE_FILE = 'database.db'
database = Db(DATABASE_FILE)
  
while(True): 
    # Open database
    database.openDB(DATABASE_FILE)

    # Get page content
    driver.get("http://www.retroradio.hu/")
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features="html.parser")

    # Search for title and artist
    artist = soup.find("span", {"class": "js-radio-player-current-artist"})
    title = soup.find("span", {"class": "js-radio-player-current-title"})

    # Add song to database
    database.addSong(artist.text, title.text)

    # Close database
    database.closeDB()

    # Sleep 100s and get new content after
    time.sleep(100) 

