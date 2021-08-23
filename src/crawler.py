from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def crawl(address, load_time, chrome_path, driver_path):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    #options.binary_location = chrome_path
    driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
    driver.delete_all_cookies()
    driver.get(address)
    time.sleep(load_time)
    driver.close()
