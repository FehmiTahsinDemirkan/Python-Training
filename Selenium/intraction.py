from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\chromedriver"

driver = webdriver.Chrome()

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

articleCountbtn = driver.find_elements(By.CLASS_NAME, 'main-top-articleCount a')[1]



tumPortallar = driver.find_element(by='link text',value='Daha fazla seçkin madde')
tumPortallar.click()


searchInput = driver.find_element(by='name',value='search')
searchInput.send_keys("Python")
searchInput.send_keys(Keys.ENTER)

login = driver.find_element(by='css selector',value='#pt-login-2')
login.click()



username = driver.find_element(by='id',value='wpName1')
username.send_keys("Fehmi")

password = driver.find_element(by='id',value='wpPassword1')
password.send_keys("AAAA")

remember = driver.find_element(by='id',value='wpRemember')
remember.click()

btn = driver.find_element(by='id',value='wpLoginAttempt')
btn.click()


