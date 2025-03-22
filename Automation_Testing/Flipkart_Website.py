from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time
import pandas as pd

driver = webdriver.Chrome()
driver.maximize_window()

# Opening DuckDuckGo as a Search engine
driver.get("https://duckduckgo.com")

# Search Flipkart
elem = driver.find_element(By.XPATH, '//*[@id="searchbox_input"]')
elem.send_keys('Flipkart')
elem.send_keys(Keys.RETURN)
time.sleep(5)
elem = driver.find_element(By.XPATH, '//*[@id="r1-0"]/div[3]/h2/a/span').click()
time.sleep(5)

#Scroll the webpage 
driver.execute_script('window.scroll(0,200)')
time.sleep(3)

# Product link
elem = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/a/div/div/div[2]/div[2]').click()
time.sleep(10)

# Get the product name and product price using CLASS_NAMEs
elem2 = driver.find_elements(By.CLASS_NAME, 'wjcEIp')  # Product names
elem3 = driver.find_elements(By.CLASS_NAME, 'Nx9bqj')  # Product prices

# Initialize lists to store the names and prices
names = []
prices = []

# Extract the text 
for product_name, product_price in zip(elem2, elem3):
    names.append(product_name.text)  # Extract text from the WebElement
    prices.append(product_price.text)  # Extract text from the WebElement

# Create a DataFrame with the names and prices
df = pd.DataFrame(zip(names, prices), columns=['name', 'price'])

# Save the data to an Excel file
df.to_excel("data.xlsx", index=False)

# Sleep for 10 seconds to observe the result before closing
time.sleep(10)
driver.quit()
