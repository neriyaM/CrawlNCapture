from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def crawl(address, load_time):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.delete_all_cookies()
    driver.get(address)
    time.sleep(load_time)
    driver.close()
