from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
for i in range(1 , 20):
    driver.get(f"https://www.amazon.com/s?k={laptop}&page={i}&xpid=RX5_8PthrQKqR&crid=1UPZWEA35E9Z9&qid=1764676233&sprefix=laptop%2Caps%2C355&ref=sr_pg_2")

    elems = driver.find_element(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elem)
time.sleep(6)
driver.close()