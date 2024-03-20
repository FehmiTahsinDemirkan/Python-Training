from selenium import  webdriver
import time
chrome_driver_path = "C:\chromedriver"

driver = webdriver.Chrome()

url = "https://github.com/"

driver.get(url)
time.sleep(1)
driver.maximize_window()
driver.save_screenshot("github.png")
driver.get(url+"FehmiTahsinDemirkan")

print(driver.title)
time.sleep(2)
driver.back()
driver.close()