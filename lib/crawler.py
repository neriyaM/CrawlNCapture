from selenium import webdriver
import time


def crawl(address, load_time):
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.get(address)
    time.sleep(load_time)
    driver.close()
