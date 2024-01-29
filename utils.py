import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    service = Service('../chromedriver')
    driver = webdriver.Chrome(service=service)

    return driver


def get_soup_by_selenium_driver(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    return soup
