#This is an auto cookie clicker bot but it's really inneficcient 😭😭😭
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

for i in range(10):
    cookie.click()

c1,c2,c3,c4,c5,c6,c7,c0,c8=0,0,0,0,0,0,0,0,0
while True:
    for i in range(1000):
        cookie.click()
    wealth=int(''.join([i for i in (count.text.split(" ")[0]) if i.isnumeric()]))
    try:
        price=driver.find_element(By.ID, "productPrice8")
        if wealth>int(price.text) and c0<10:
            c0+=1
            upgrade=driver.find_element(By.ID, "product8")
            upgrade.click()
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice7")
        if wealth>int(price.text) and c1<10:
            c1+=1
            upgrade=driver.find_element(By.ID, "product7")
            upgrade.click()
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice6")
        price=int(''.join([i for i in price.text if i.isnumeric()]))
        if wealth>int(price) and c2<10:
            c2+=1
            upgrade=driver.find_element(By.ID, "product6")
            upgrade.click()
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice5")
        price=int(''.join([i for i in price.text if i.isnumeric()]))
        if wealth>int(price) and c3<10:
            c3+=1
            upgrade=driver.find_element(By.ID, "product5")
            upgrade.click()
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice4")
        price=int(''.join([i for i in price.text if i.isnumeric()]))
        if wealth>int(price) and c4<10:
            c4+=1
            upgrade=driver.find_element(By.ID, "product4")
            upgrade.click()
            print("Factory Bought")
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice3")
        price=int(''.join([i for i in price.text if i.isnumeric()]))
        if wealth>int(price) and c5<10:
            c5+=1
            upgrade=driver.find_element(By.ID, "product3")
            upgrade.click()
            print("Mine Bought")
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice2")
        price=int(''.join([i for i in price.text if i.isnumeric()]))
        if wealth>int(price) and c6<10:
            c6+=1
            upgrade=driver.find_element(By.ID, "product2")
            upgrade.click()
            print("Farm Bought")
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice1")
        price=int(''.join([i for i in price.text if i.isnumeric()]))
        if wealth>int(price) and c7<10:
            c7+=1
            upgrade=driver.find_element(By.ID, "product1")
            upgrade.click()
            print("Grandma Bought")
    except:
        pass
    try:
        price=driver.find_element(By.ID, "productPrice0")
        price=int(''.join([i for i in price.text if i.isnumeric()]))
        if wealth>int(price) and c8<10:
            c8+=1
            upgrade=driver.find_element(By.ID, "product0")
            upgrade.click()
            print("Cursor Bought")
    except:
        pass