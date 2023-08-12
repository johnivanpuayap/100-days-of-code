from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Using Selenium with a webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://en.wikipedia.org/wiki/Main_Page/')

# Using ID
count_element = driver.find_element(By.ID, 'articlecount')
count = count_element.find_element(By.TAG_NAME, 'a')
print(count.text)

# Using XPath
count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
print(count)

# Using CSS Selector
count = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text
print(count)

driver.quit()