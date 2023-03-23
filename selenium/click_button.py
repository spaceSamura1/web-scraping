#Goal: How to find elements with Selenium
from selenium import webdriver
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/ging/Documents/coding/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
all_matches_button.click()

time.sleep(10)

# driver.quit()