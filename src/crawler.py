from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dataclasses import asdict
import time


def crawl(address, load_time, chrome_path, driver_path, cookies):
    options = Options()
    options.binary_location = chrome_path
    driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
    driver.get(address)
    for cookie in cookies:
        driver.add_cookie(asdict(cookie))
    print(driver.get_cookies())
    driver.get(address)
    time.sleep(load_time)
    driver.close()
