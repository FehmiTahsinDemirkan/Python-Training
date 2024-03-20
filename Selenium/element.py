from selenium import webdriver

chrome_driver_path = "C:\chromedriver"

driver = webdriver.Chrome()

url = "https://www.n11.com/urun/heinz-ketcap-570-g-51170446?magaza=heinz"

driver.get(url)

title = driver.find_element(by='class name', value='proName').text
price = driver.find_element(by='class name',value='newPrice').find_element(by='tag name',value='ins').text
print(title)
print(price)

driver.close()
