from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pprint import pprint

# Using Selenium with a webdriver_manager so that you won't need to download a driver everytime a new version comes out
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

events_dict = {}

driver.get('https://www.python.org')
events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

for count, event in enumerate(events, start=0):
    time_element = event.find_element(By.TAG_NAME, 'time')
    time = time_element.get_attribute('datetime').split('T')[0]
    name_element = event.find_element(By.TAG_NAME, 'a')
    name = name_element.text
    events_dict[count] = {'time': time, 'name': name}

pprint(events_dict)

driver.quit()