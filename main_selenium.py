from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display

import scraper

print("Creating display driver object...")
display = Display(visible=0, size=(800, 600))

print("Starting driver...")
display.start()

print("Loading Chrome...")
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

print("Loading webpage...")
driver.get('https://www.swedavia.se/arlanda/sakerhetskontroll/')

print("Parsing html...")
scraper.parse_tree(driver.page_source)
driver.quit()
