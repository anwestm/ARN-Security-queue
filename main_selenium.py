from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display

import schedule
import time
import datetime
import scraper

def load_site():
    print("Loading webpage...")
    driver.get('https://www.swedavia.se/arlanda/sakerhetskontroll/')

    print("Parsing html...")
    scraper.parse_tree(driver.page_source)

print("Creating display driver object...")
display = Display(visible=0, size=(800, 600))

print("Starting driver...")
display.start()

print("Loading Chrome...")
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

schedule.every(5).minutes.do(load_site)
while True:
    schedule.run_pending()
    time.sleep(1)


driver.quit()
