from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from userinfo import username, password
import time
import atexit

class Github:
    chrome_driver_path = "C:\chromedriver"

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.baseUrl = "https://github.com/"
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get(self.baseUrl + "login")
        self.browser.find_element(by='name', value='login').send_keys(self.username)
        self.browser.find_element(by='name', value='password').send_keys(self.password)
        self.browser.find_element(by='name', value='commit').click()

    # def findRepositories(self, keyword):
    #     self.browser.get(self.baseUrl)
    #     searchInput = self.browser.find_element(by='name', value='query-builder-test')
    #     searchInput.send_keys(keyword)
    #     searchInput.send_keys(Keys.ENTER)

    def getFollowers(self):
        self.browser.get(f"{self.baseUrl}{self.username}?tab=followers")
        items = self.browser.find_element(by='css selector',value='.d-table.table-fixed')

        for item in items:
            print(item)
    def close(self):
        self.browser.quit()

app = Github()
# app.signIn()
app.getFollowers()
# app.findRepositories("python")
