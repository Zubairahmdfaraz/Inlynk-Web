import time
import unittest
import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ConfigurationPage import ConfigurationPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestConfiguration(unittest.TestCase):
    baseURL = ReadConfig.getApplicationURL()

    DeptName = "QA"
    DeptDescription = "Software Testing"
    EditDeptDescription = "Software Testing test data"
    DivisionName = "Manual Testing"
    DivisionDescription = "Functional and Non Functional"
    EditDivisionDescription = "Functional and Non Functional test data"
    DesignationName = "Associate Test Engineer"
    DesignationDescription = "All testing activities"
    EditDesignationDescription = "All testing activities test data"

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger = LogGen.loggen()

    def setUp(self):
        self.logger = LogGen.loggen()
        self.driver = webdriver.Chrome()  # Change to the appropriate driver
        self.driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.regression
    def test_createDept(self):
        self.logger.info("****Started Login Test****")
        # self.driver = setup
        self.driver.get(self.baseURL)
        # self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.cp = ConfigurationPage(self.driver)
        self.cp.clickModuleConfiguration()
        self.cp.clickDepartments()
        self.logger.info(" Started TC_01 : Verify create NEW Department ")
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DeptName)
        self.cp.setEnterDescription(self.DeptDescription)
        self.cp.clickCreateBtn()
        time.sleep(3)
        act_Text = self.cp.Text_DeptCreatedSuccessful()
        if act_Text == "Department created successfully":
            assert True
            self.logger.info("********* TC_01 : Verify create NEW Department Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
            self.logger.error("********* TC_01 : Verify create NEW Department Test is Failed ***********")
            self.driver.close()
            assert False
        self.logger.info(" Started TC_04 : Verify Search Department ")
        self.cp.setsearchField(self.DeptName)
        self.cp.clickopenDept()
        self.logger.info(" Started TC_06 : Verify create NEW Division ")
        self.cp.clickDivisionsTab()
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DivisionName)
        self.cp.setEnterDescription(self.DivisionDescription)
        self.cp.clickCreateBtn()
        time.sleep(3)
        act_Text = self.cp.Text_DivisionCreatedSuccessful()
        if act_Text == "Division created successfully":
            assert True
            self.logger.info("********* TC_06 : Verify create NEW Division Test is Passed ***********")

        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
            self.logger.error("********* Create Division Test is Failed ***********")
            self.driver.close()
            assert False

        self.cp.clickDesignationsTab()
        self.logger.info(" Started TC_10 : Verify Create NEW Designation ")
        self.cp.clickNewBtn()
        self.cp.setDepartmentName(self.DesignationName)
        self.cp.setEnterDescription(self.DesignationDescription)
        self.cp.clickCreateBtn()
        time.sleep(3)
        act_Text = self.cp.Text_DesignationCreatedSuccessful()
        if act_Text == "Designation created successfully":
            assert True
            self.logger.info("********* Create Designation Test is Passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "TC_10_test_createDept.png")
            self.logger.error("********* TC_10 : Verify Create NEW Designation Test is Failed ***********")
            self.driver.close()
            assert False

    # @pytest.mark.regression
    # def test_EditDept(self, setup):
    #     self.logger.info("****Started Login Test****")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     self.lp.clickNewsFeed()
    #     self.cp = ConfigurationPage(self.driver)
    #     self.cp.clickModuleConfiguration()
    #     self.cp.clickDepartments()
    #     self.cp.clickDepartments()
    #     time.sleep(3)
    #     self.cp.setsearchField(self.DeptName)
    #     time.sleep(2)
    #     self.cp.clickEditDepartment()
    #     self.cp.setEnterDescription(self.EditDeptDescription)
    #     time.sleep(1)
    #     self.cp.clickUpdateBtn()
    #     time.sleep(3)
    #     act_Text = self.cp.Text_DeptUpdatedSuccessful()
    #     if act_Text == "Department updated successfully":
    #         assert True
    #         self.logger.info("********* updated Department Test is Passed ***********")
    #
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
    #         self.logger.error("********* updated Department Test is Failed ***********")
    #         self.driver.close()
    #         assert False
    #
    #     self.cp.setsearchField(self.DeptName)
    #     self.cp.clickopenDept()
    #     self.cp.clickDivisionsTab()
    #     self.cp.setsearchField(self.DivisionName)
    #     time.sleep(2)
    #     self.cp.clickEditDivision()
    #     self.cp.setEnterDescription(self.EditDivisionDescription)
    #     self.cp.clickUpdateBtn()
    #     time.sleep(3)
    #     act_Text = self.cp.Text_DivisionUpdatedSuccessful()
    #     if act_Text == "Division updated successfully":
    #         assert True
    #         self.logger.info("********* updated Division Test is Passed ***********")
    #
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
    #         self.logger.error("********* updated Division Test is Failed ***********")
    #         self.driver.close()
    #         assert False
    #
    #     self.cp.clickDesignationsTab()
    #     self.cp.setsearchField(self.DesignationName)
    #     self.cp.clickEditDivision()
    #     time.sleep(2)
    #     self.cp.setEnterDescription(self.EditDesignationDescription)
    #     self.cp.clickUpdateBtn()
    #     time.sleep(3)
    #     act_Text = self.cp.Text_DesignationUpdatedSuccessful()
    #     if act_Text == "Designation updated successfully":
    #         assert True
    #         self.logger.info("********* updated Designation Test is Passed ***********")
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
    #         self.logger.error("********* updated Designation Test is Failed ***********")
    #         self.driver.close()
    #         assert False
    #
    # @pytest.mark.regression
    # def test_DeleteDept(self, setup):
    #     self.logger.info("****Started Login Test****")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.driver.maximize_window()
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     self.lp.clickNewsFeed()
    #     self.cp = ConfigurationPage(self.driver)
    #     self.cp.clickModuleConfiguration()
    #     self.cp.clickDepartments()
    #     time.sleep(3)
    #     self.cp.setsearchField(self.DeptName)
    #     time.sleep(2)
    #     self.cp.clickDeleteDepartment()
    #     self.cp.clickDeleteDepartmentDelete()
    #     time.sleep(2)
    #     act_Text = self.cp.Text_DeleteError()
    #     if act_Text == "Some Division Under This Department":
    #         assert True
    #         self.logger.info("********* Delete Error Designation Test is Passed ***********")
    #
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
    #         self.logger.error("********* Delete Error Designation Test is Failed ***********")
    #         self.driver.close()
    #         assert False
    #     self.cp.clickDeleteDepartmentCancel()
    #
    #
    #     self.cp.clickopenDept()
    #     self.cp.clickDivisionsTab()
    #     self.cp.setsearchField(self.DivisionName)
    #     time.sleep(2)
    #     self.cp.clickDeleteDivision()
    #     self.cp.clickDeleteDepartmentDelete()
    #     time.sleep(2)
    #     act_Text = self.cp.Text_DivisionDeletedSuccessfully()
    #     if act_Text == "Division deleted successfully":
    #         assert True
    #         self.logger.info("********* Delete Division Test is Passed ***********")
    #
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
    #         self.logger.error("********* Delete Division Test is Failed ***********")
    #         self.driver.close()
    #         assert False
    #
    #     self.cp.clickDesignationsTab()
    #     self.cp.setsearchField(self.DesignationName)
    #     # time.sleep(4)
    #     self.cp.clickDeleteDivision()
    #     self.cp.clickDeleteDepartmentDelete()
    #     time.sleep(2)
    #     act_Text = self.cp.Text_DesignationDeletedSuccessfully()
    #     if act_Text == "Designation deleted successfully":
    #         assert True
    #         self.logger.info("********* Delete Designation Test is Passed ***********")
    #
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
    #         self.logger.error("********* Delete Designation Test is Failed ***********")
    #         self.driver.close()
    #         assert False
    #
    #     # Use the browser's back button to navigate back
    #     self.cp.clickConfigurationtextLink()
    #
    #     # Wait for a few seconds (for demonstration purposes)
    #     time.sleep(3)
    #
    #     self.cp.setsearchField(self.DeptName)
    #     time.sleep(2)
    #     self.cp.clickDeleteDepartment()
    #     self.cp.clickDeleteDepartmentDelete()
    #     time.sleep(2)
    #     act_Text = self.cp.Text_DepartmentDeletedSuccessfully()
    #     if act_Text == "Department deleted successfully":
    #         assert True
    #         self.logger.info("********* Delete Department Test is Passed ***********")
    #
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\" + "test_createDept.png")
    #         self.logger.error("********* Delete Department Test is Failed ***********")
    #         self.driver.close()
    #         assert False

    if __name__ == '__main__':
        unittest.main(verbosity=2)