import os

import pytest
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from krishnapageObjects.NewsfeedPage import NewsFeed
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_NewsFeed:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    whats = ReadConfig.getwhats()
    whatso = ReadConfig.getwhatso()
    usernames = ReadConfig.getuseremails()
    usernames1 = ReadConfig.getuseremails1()
    usernames2 = ReadConfig.getuseremails2()
    usernames3 = ReadConfig.getuseremails3()
    whatson = ReadConfig.getwhatson()
    oneimage = ReadConfig.getoneimage()
    fiveimages = ReadConfig.getfiveimages()
    relative_one = "Files/one.png"
    absolute_path1 = os.path.abspath(relative_one)
    relative_two = "Files/two.png"
    absolute_path2 = os.path.abspath(relative_two)
    relative_three = "Files/three.png"
    absolute_path3 = os.path.abspath(relative_three)
    relative_four = "Files/four.png"
    absolute_path4 = os.path.abspath(relative_four)
    relative_five = "Files/five.png"
    absolute_path5 = os.path.abspath(relative_five)
    relative_six = "Files/six.jpg"
    absolute_path6 = os.path.abspath(relative_six)
    relative_video1 = "Files/video1.mp4"
    absolute_pathvideo1 = os.path.abspath(relative_video1)
    whatvideo = ReadConfig.getwhatvideo()
    relative_video2 = "Files/video2.mp4"
    absolute_pathvideo2 = os.path.abspath(relative_video2)
    whatvideos = ReadConfig.getwhatvideos()
    whatyoutube = ReadConfig.getwhatyoutube()
    youtubeurl = ReadConfig.getyoutubeurl()
    whatedit = ReadConfig.getwhatedit()
    commenttext = "hiii gud mrng"
    replytext = "gudmorning all"
    commentedittext = "all "


    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforemployees(self, setup):
         self.logger.info("************* Test_003_NewsFeed **********")
         self.driver = setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()

         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         self.logger.info("************* Login succesful **********")

         self.logger.info("******* Starting NewsFeed Test **********")
         self.nf = NewsFeed(self.driver)
         time.sleep(3)
         self.nf.clickOnwhat()
         time.sleep(3)
         self.nf.setwhats(self.whats)
         time.sleep(3)
         self.nf.clickonpost()
         time.sleep(3)
         if "News feed created successfully" in self.driver.page_source:
             self.logger.info("********** NewsFeed test is passed *********")

         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed test is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
             assert False
         time.sleep(3)
         self.nf.clickonlogout()
         self.logger.info("************* Logout succesful **********")
         time.sleep(3)
         self.lp.setUserNames(self.usernames)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         time.sleep(3)
         self.logger.info("************* EmpLogin succesful **********")
         if "Hi,gud mrng employees" in self.driver.page_source:
             self.logger.info("********** NewsFeed display is passed *********")
             self.driver.close()
         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed display is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
             assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforempndrel(self, setup):
         self.logger.info("************* Test_003_NewsFeed **********")
         self.driver = setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()

         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         self.logger.info("************* Login succesful **********")

         self.logger.info("******* Starting NewsFeed Test **********")
         self.nf = NewsFeed(self.driver)
         time.sleep(3)
         self.nf.clickOnwhat()
         time.sleep(3)
         self.nf.setwhatso(self.whatso)
         time.sleep(3)
         self.nf.clickonpublic()
         time.sleep(3)
         self.nf.clickonpost()
         time.sleep(3)
         if "News feed created successfully" in self.driver.page_source:
             self.logger.info("********** NewsFeed test is passed *********")

         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed test is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
             assert False
         time.sleep(3)
         self.nf.clickonlogout()
         self.logger.info("************* Logout succesful **********")
         time.sleep(3)
         self.lp.setUserNames1(self.usernames1)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         time.sleep(3)
         self.logger.info("************* relationcompanyLogin succesful **********")
         if "hii,all employees and relation companies" in self.driver.page_source:
             self.logger.info("********** NewsFeed display is passed *********")
             self.driver.close()
         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed display is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
             assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforpartners(self, setup):
         self.logger.info("************* Test_003_NewsFeed **********")
         self.driver = setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()

         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         self.logger.info("************* Login succesful **********")

         self.logger.info("******* Starting NewsFeed Test **********")
         self.nf = NewsFeed(self.driver)
         time.sleep(3)
         self.nf.clickOnwhat()
         time.sleep(3)
         self.nf.setwhatson(self.whatson)
         time.sleep(3)
         self.nf.clickonemp()
         time.sleep(3)
         self.nf.clickonpartner()
         time.sleep(3)
         self.nf.clickonpost()
         time.sleep(3)
         if "News feed created successfully" in self.driver.page_source:
             self.logger.info("********** NewsFeed test is passed *********")

         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed test is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed3.png")
             assert False
         time.sleep(3)
         self.nf.clickonlogout()
         self.logger.info("************* Logout succesful **********")
         time.sleep(3)
         self.lp.setUserNames2(self.usernames2)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         time.sleep(3)
         self.logger.info("************* partnerLogin succesful **********")
         if "hii,all partners schedule the meeting" in self.driver.page_source:
             self.logger.info("********** NewsFeed display is passed *********")
             self.driver.close()
         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed display is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed3.png")
             assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforarchived(self, setup):
         self.logger.info("************* Test_003_NewsFeed **********")
         self.driver = setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()

         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         self.logger.info("************* Login succesful **********")

         self.logger.info("******* Starting NewsFeed Test **********")
         self.nf = NewsFeed(self.driver)
         time.sleep(3)
         self.nf.clickOnwhat()
         time.sleep(3)
         self.nf.setwhats(self.whats)
         time.sleep(3)
         self.nf.clickonstatus()
         time.sleep(3)
         self.nf.clickonpost()
         time.sleep(3)
         if "Post created and saved in archived list" in self.driver.page_source:
             self.logger.info("********** NewsFeed test is passed *********")

         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed test is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed4.png")
             assert False
         time.sleep(3)
         self.nf.clickonthreedots()
         time.sleep(3)
         self.nf.clickonarchive()
         time.sleep(3)
         if "Hi,gud mrng employees" in self.driver.page_source:
             self.logger.info("********** NewsFeed test is passed *********")

         else:
             # Log and take a screenshot
             self.logger.error("************** NewsFeed test is failed **********")
             self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed4.png")
             assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwithimage(self, setup):
         self.logger.info("************* Test_003_NewsFeed **********")
         self.driver = setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()

         self.lp = LoginPage(self.driver)
         self.lp.setUserName(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         self.logger.info("************* Login succesful **********")

         self.logger.info("******* Starting NewsFeed Test **********")
         self.nf = NewsFeed(self.driver)
         time.sleep(3)
         self.nf.clickOnwhat()
         time.sleep(3)
         self.nf.setoneimage(self.oneimage)
         time.sleep(3)
         self.nf.setgallery(self.absolute_path1)
         time.sleep(3)
         self.nf.clickonpost()
         time.sleep(3)
         if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

         else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed5.png")
            assert False
         self.nf.clickonlogout()
         self.logger.info("************* Logout succesful **********")
         time.sleep(3)
         self.lp.setUserNames(self.usernames)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         time.sleep(3)
         self.logger.info("************* EmpLogin succesful **********")
         time.sleep(3)
         if "one image upload" in self.driver.page_source:
            self.logger.info("***************Newsfeed test is passed **********")

         else:
            self.logger.error("************* NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed5.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwith5images(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setfiveimages(self.fiveimages)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path1)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path2)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path3)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path4)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path5)
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed6.png")
            assert False
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserNames(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin succesful **********")
        self.nf.clickonimage()
        time.sleep(3)
        if "five images upload" in self.driver.page_source:
            self.logger.info("***************Newsfeed test is passed **********")

        else:
            self.logger.error("************* NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed6.png")
            assert False



    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwith6images(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setgallery(self.absolute_path1)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path2)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path3)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path4)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path5)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path6)
        # self.nf.clickonpost()
        time.sleep(3)
        if "Cannot upload more than 5 images" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed7.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwithimages(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setfiveimages(self.fiveimages)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path1)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path2)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path3)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path4)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path5)
        time.sleep(3)
        self.nf.clickonpublic()
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed8.png")
            assert False
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserNames1(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin succesful **********")
        self.nf.clickonimage()
        time.sleep(3)
        if "five images upload" in self.driver.page_source:
            self.logger.info("***************Newsfeed test is passed **********")

        else:
            self.logger.error("************* NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed8.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")

    def test_newsfeedforemployeesvideo(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhats(self.whatvideo)
        time.sleep(3)
        self.nf.setvideo(self.absolute_pathvideo1)
        time.sleep(3)
        # self.nf.clickonpost()
        if "Cannot upload greater than 20MB" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforemployeesvideos(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhats(self.whatvideos)
        time.sleep(3)
        self.nf.setvideo(self.absolute_pathvideo2)
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserNames(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin succesful **********")
        if "uploading videos" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforempndrelvideo(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhatyoutube(self.whatyoutube)
        time.sleep(3)
        self.nf.clickonpublic()
        time.sleep(3)
        self.nf.clickonyoutube()
        time.sleep(3)
        self.nf.setyoutubeurl(self.youtubeurl)
        time.sleep(3)
        self.nf.clickondone()
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserNames1(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "uploading youtube videos" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_editnewsfeedforemployees(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhats(self.whats)
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(5)
        self.nf.clickonthreedot()
        time.sleep(3)
        self.nf.clickonedit()
        time.sleep(3)
        self.nf.setwhatedit(self.whatedit)
        time.sleep(3)
        self.nf.clickonpublic()
        time.sleep(3)
        self.nf.clickonupdate()
        time.sleep(3)
        if "News feed updated successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserNames1(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "Hi,gud mrng employeesEditing the feed" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_deletenewsfeedforempndrelvideo(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhatyoutube(self.whatyoutube)
        time.sleep(3)
        self.nf.clickonpublic()
        time.sleep(3)
        self.nf.clickonyoutube()
        time.sleep(3)
        self.nf.setyoutubeurl(self.youtubeurl)
        time.sleep(3)
        self.nf.clickondone()
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedot()
        time.sleep(3)
        self.nf.clickondelete()
        time.sleep(3)
        self.nf.clickondeletecheckbox()
        time.sleep(3)
        self.nf.clickondeletebutton()
        time.sleep(3)
        if "News Feed deleted successfully!" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_archivenewsfeedwith5images(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setfiveimages(self.fiveimages)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path1)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path2)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path3)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path4)
        time.sleep(3)
        self.nf.setgallery(self.absolute_path5)
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed6.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedot()
        time.sleep(3)
        self.nf.clickondelete()
        time.sleep(3)
        self.nf.clickondeletebutton()
        time.sleep(3)
        if "Feed deleted successfully, saved in archived feed" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed6.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedots()
        time.sleep(3)
        self.nf.clickonarchive()
        time.sleep(3)
        if "five images upload" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed4.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_bookmarknewsfeed(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhatso(self.whatso)
        time.sleep(3)
        self.nf.clickonpublic()
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickonthreedot()
        time.sleep(3)
        self.nf.clickonbookmark()
        time.sleep(3)
        self.nf.clickonexplore()
        time.sleep(3)
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        self.nf.clickonremove()
        time.sleep(3)
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.error("********** NewsFeed test is failed *********")
            # Log and take a screenshot
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False


        else:
            self.logger.info("************** NewsFeed test is passed **********")
        time.sleep(3)

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_selfposts(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhatso(self.whatso)
        time.sleep(3)
        self.nf.clickonpublic()
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        self.nf.clickonthreedots()
        time.sleep(3)
        self.nf.clickonfilter()
        time.sleep(3)
        self.nf.clickonall()
        time.sleep(3)
        self.nf.clickonself()
        time.sleep(3)
        self.nf.clickonapply()
        time.sleep(3)
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_sharenewsfeed(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        time.sleep(0.5)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(0.5)
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(1)
        self.nf.clickOnwhat()
        time.sleep(0.5)
        self.nf.setwhatso(self.whatso)
        time.sleep(0.5)
        self.nf.clickonpublic()
        time.sleep(0.5)
        self.nf.clickonpost()
        time.sleep(0.5)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(0.5)
        self.nf.clickonshare()
        time.sleep(0.5)
        self.nf.clickonwhatsapp()
        time.sleep(0.5)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(3)

        if "https://web.whatsapp.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        # Switch to the last opened window
        self.driver.switch_to.window(window_handles[0])
        time.sleep(2)
        self.nf.clickonshare()
        time.sleep(3)
        self.driver.implicitly_wait(5)
        self.nf.clickonfacebook()
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[2])
        time.sleep(3)

        if "https://www.facebook.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        time.sleep(3)
        self.nf.clickonshare()
        time.sleep(2)
        self.nf.clickontwitter()
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[3])
        time.sleep(3)

        if "https://twitter.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        time.sleep(3)
        self.nf.clickonshare()
        time.sleep(2)
        self.nf.clickonlinkedin()
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[4])
        time.sleep(3)

        if "https://www.linkedin.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        time.sleep(3)
        self.nf.clickonshare()
        time.sleep(2)
        self.nf.clickontelegram()
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[5])
        time.sleep(3)

        if "https://telegram.me/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        time.sleep(3)
        self.nf.clickonshare()
        time.sleep(2)
        self.nf.clickongmail()
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[6])
        time.sleep(3)

        if "https://accounts.google.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")
        elif "https://www.google.com/" in self.driver.current_url:
            # Handle the other condition
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[0])
        time.sleep(3)
        # self.nf.clickonshare()
        # time.sleep(2)
        self.nf.clickoninstagram()
        time.sleep(3)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[7])
        time.sleep(3)

        if "https://www.instagram.com/" in self.driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_adminfeed(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserNames3(self.usernames3)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhatso(self.whatso)
        time.sleep(3)
        self.nf.clickonpublic()
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False
        time.sleep(3)
        self.nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.lp.setUserNames1(self.usernames1)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "hii,all employees and relation companies" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            self.driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_feedcomment(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhats(self.whats)
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.nf.clickoncomment()
        time.sleep(3)
        self.nf.setcommenttext(self.commenttext)
        time.sleep(3)
        self.nf.clickonsend()
        time.sleep(3)
        self.nf.clickoncancelcmnt()
        time.sleep(3)
        self.nf.clickonlogout()
        time.sleep(3)
        self.logger.info("************* Logout succesful **********")
        time.sleep(3)
        self.driver.execute_script("window.open('', '_blank');")
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(3)
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp.setUserNames(self.usernames)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin succesful **********")
        if "Hi,gud mrng employees" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.nf.clickoncomments()
        time.sleep(3)
        self.nf.clickonreplycmnt()
        time.sleep(3)
        self.nf.setreplytext(self.replytext)
        time.sleep(3)
        self.nf.clickonreplysend()
        time.sleep(3)
        self.nf.clickonviewreply()
        time.sleep(3)
        if "gudmorning all" in self.driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    # @pytest.mark.skip(reason="Skipping this test")
    def test_editfeedcomment(self, setup):
        self.logger.info("************* Test_003_NewsFeed **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        self.nf = NewsFeed(self.driver)
        time.sleep(3)
        self.nf.clickOnwhat()
        time.sleep(3)
        self.nf.setwhats(self.whats)
        time.sleep(3)
        self.nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in self.driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed1.png")
            assert False
        time.sleep(3)
        self.nf.clickoncomment()
        time.sleep(3)
        self.nf.setcommenttext(self.commenttext)
        time.sleep(3)
        self.nf.clickonsend()
        time.sleep(3)
        self.nf.clickoncommentthreedot()
        time.sleep(3)
        self.nf.clickoncommentedit()
        time.sleep(3)
        self.nf.setcommentedittext(self.commentedittext)
        time.sleep(3)
        self.nf.clickoncommenteditsend()
        time.sleep(3)
        self.nf.clickoncommentthreedot()
        time.sleep(3)
        self.nf.clickoncommentdelete()
        time.sleep(3)
        self.nf.clickoncommentconfirmdelete()
        time.sleep(3)
        if "all hiii gud mrng" in self.driver.page_source:
            self.logger.error("********** NewsFeed test is failed *********")
            # Log and take a screenshot
            self.driver.save_screenshot(".\\Screenshots\\" + "test_newsfeed2.png")
            assert False


        else:
            self.logger.info("************** NewsFeed test is passed **********")
        time.sleep(3)








































