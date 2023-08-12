from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Using Selenium with a webdriver_manager so that you won't need to download a driver everytime a new version comes out

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Get the Price of a Product in Amazon
# driver.get('https://www.amazon.com/Dowinx-Ergonomic-Computer-Comfortable-Reclining/dp/B0C58F2LQQ/ref=sr_1_8?keywords'
#            '=gaming%2Bchair&qid=1691849150&sprefix=gaming%2Caps%2C879&sr=8-8&th=1')
# price = driver.find_element(By.CLASS_NAME, 'aok-offscreen')
# print(price.text)

# Find the Element by name
# driver.get('https://www.python.org/')
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# Find the Element using the CSS Selector
# driver.get('https://www.amazon.com/Dowinx-Ergonomic-Computer-Comfortable-Reclining/dp/B0C58F2LQQ/ref=sr_1_8?keywords'
#            '=gaming%2Bchair&qid=1691849150&sprefix=gaming%2Caps%2C879&sr=8-8&th=1')
# price = driver.find_element(By.CSS_SELECTOR, '.a-section a-spacing-none aok-align-center aok-relative .aok-offscreen')
# print(price.text)

# Find the Element using the XPath
# XPath is a surefire way of finding an element in an HTML file
driver.get('https://www.amazon.com/Dowinx-Ergonomic-Computer-Comfortable-Reclining/dp/B0C58F2LQQ/ref=sr_1_8?keywords'
           '=gaming%2Bchair&qid=1691849150&sprefix=gaming%2Caps%2C879&sr=8-8&th=1')
price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]')
print(price.text)


# Close vs Quit
# Close will close that particular tab
# Quit will quit the entire program
# driver.close()
driver.quit()