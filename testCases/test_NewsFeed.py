import time

import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ConfigurationPage import ConfigurationPage
from pageObjects.NewsFeedPage import NewsFeedPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Create_NewsFeed:
    baseURL = ReadConfig.getApplicationURL()

    # RelationName = "Test Dealer"
    # RelationDescription = "Test Dealer Software Testing"
    # EditRelationDescription = " Edited Description for relation"


    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_CreatePost(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.np = NewsFeedPage(self.driver)
        self.np.clickcreatePost()
