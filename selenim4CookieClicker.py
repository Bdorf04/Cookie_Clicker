#Automatic Cookie Clicker Bot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/") 

driver.implicitly_wait(2)
lang=driver.find_element(By.ID, "langSelect-EN")
lang.click()

time.sleep(4)

count=driver.find_element(By.ID, "cookies")
cookie=driver.find_element(By.ID, "bigCookie")


for i in range(700):
    cookie.click()

upgrade=driver.find_element(By.ID, "product0")  #buying 10 Clickers
for i in range(10):
    upgrade.click()

for i in range(10):
    cookie.click()

driver.find_element(By.CSS_SELECTOR, ".crate.upgrade.enabled").click()  #Buying first cursor upgrade

for i in range(500):
    cookie.click()

upgrade=driver.find_element(By.ID, "product1")  #buying 10 grandmas
for i in range(10):
    upgrade.click()

for i in range(500):
    cookie.click()

for i in range(2):
    driver.find_element(By.CSS_SELECTOR, ".crate.upgrade.enabled").click()  #Buying 2 upgrades'
    driver.implicitly_wait(2)

for i in range(5000):
    cookie.click()
print('right behin the farms')
upgrade=driver.find_element(By.ID, "product2")  #Buying 10 Farms
for i in range(10):
    upgrade.click()
print("bought the farms")
for i in range(5000):
    cookie.click()

driver.find_element(By.CSS_SELECTOR, ".crate.upgrade.enabled").click()  #Buying next 2 upgrades

print("We made it here!!!")
for i in range(5):
    cookie.click(10000)
    for i in range(10):
        upgrade=driver.find_element(By.ID, f"product{i+3}")
    cookie.click(10000)
    for i in range(5):
        driver.find_element(By.CSS_SELECTOR, ".crate.upgrade.enabled").click()
        driver.implicitly_wait(1)

print("Bot Ended. Simply Continue Playing!")
driver.implicitly_wait(100000)