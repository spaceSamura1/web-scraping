#Goal: Extract Data from a table

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/ging/Documents/coding/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = [] 

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team(match.find_element(By.XPATH, './td[4]').text)
    #here you are iterating over 'matches' so you start the xpath with '.' to say that you are targeting inside the tr

time.sleep(10)

# driver.quit()