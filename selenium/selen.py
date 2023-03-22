#Goal: How to find elements with Selenium

from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/ging/Documents/coding/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)




driver.quit()