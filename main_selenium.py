from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display

import schedule
import time
import datetime
import scraper

def reload_site():
    start = time.time()
    print("Reloading webpage...")
    driver.refresh()

    print("Parsing html...")
    scraper.parse_tree(driver.page_source)
    print("Parsing complete after", str(time.time()-start), "seconds.")

print("Creating display driver object...")
display = Display(visible=0, size=(800, 600))

print("Starting driver...")
display.start()

options = Options()
options.add_argument("disable-infobars")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

print("Loading Chrome...")
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", chrome_options=options)

print("Loading webpage...")
driver.get("https://www.swedavia.se/arlanda/sakerhetskontroll/")

print("Parsing html...")
scraper.parse_tree(driver.page_source)

schedule.every(1).minutes.do(reload_site)
while True:
    schedule.run_pending()
    time.sleep(1)


driver.quit()
