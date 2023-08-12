from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# Click on an Element
# count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# count.click()

# Click on a Link Text (Note: Case-Sensitive)
# all_portals = driver.find_element(By.LINK_TEXT, 'View history')
# all_portals.click()

# Typing
# search_bar = driver.find_element(By.CLASS_NAME, 'cdx-text-input__input')
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

# Signing Up
driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("John Ivan")

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys("Puayap")

email = driver.find_element(By.NAME, 'email')
email.send_keys('johnivanpuayap@gmail.com')

# You can do this
email.send_keys(Keys.ENTER)

# or this
submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

time.sleep(10)
driver.quit()