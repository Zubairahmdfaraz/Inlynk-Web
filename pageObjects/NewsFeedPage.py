from telnetlib import EC

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class NewsFeedPage:
    Button_CreateNews_xpath = "//button[contains(text(),'Create news')]"
    createPost_xpath = "//span[@class='pdngXS brdrBlackSM postWidth brdrRadiusXSM pointer lightTxt feedHover']"
    text_FeedText_xpath = "//div[@class='ql-editor ql-blank']"


    def __init__(self, driver):
        self.driver = driver

    def clickcreateNews(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Button_CreateNews_xpath)))
        element.click()
    def clickcreatePost(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.createPost_xpath)))
        element.click()