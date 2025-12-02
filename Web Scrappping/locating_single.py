from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.com/s?k=laptop&crid=1UPZWEA35E9Z9&sprefix=laptop%2Caps%2C355&ref=nb_sb_noss_1")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(elem.get_attribute("outerHTML"))
time.sleep(6)
driver.close()