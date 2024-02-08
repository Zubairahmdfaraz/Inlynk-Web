import time
# from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeesPage:
    button_employeesModule_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]"
    button_Active_xpath = "//button[normalize-space()='Active']"
    text_activeSearchField_xpath = "//input[@placeholder='Search Active Employee']"
    button_New_xpath = "//button[normalize-space()='New']"
    text_fullname_xpath = "//input[@name='fullname']"
    text_email_xpath = "//input[@id='email']"
    text_personalEmail_xpath = "//input[@id='personalEmail']"
    text_phoneNumber_xpath = "//input[@type='tel']"
    text_empId_xpath = "//input[@name='series']"
    DD_Dept_xpath = "//div[@id='demo-simple-select']"
    button_AddDept_xpath = "(//button[@type='button'])[15]"
    button_DoneAddDept_xpath = "//button[contains(text(),'Done')]"
    DD_Division_xpath = "(//div[@id='demo-simple-select'])[2]"
    button_AddDivision_xpath = "(//button[@type='button'])[17]"
    text_Division_xpath = "(//input[@id='outlined-basic'])[2]"
    DD_Designation_xpath = "(//div[@id='demo-simple-select'])[3]"
    button_AddDesignation_xpath = "(//button[@type='button'])[18]"
    DD_CountryDD_xpath = "(//button[@aria-haspopup='listbox'])[2]"
    DD_state_xpath = "//div[@id='state']"
    DD_city_xpath = "//div[@id='city']"
    button_Add_xpath = "//button[normalize-space()='Add']"
    button_Cancel_xpath = "//button[contains(text(),'Cancel')]"
    Verify_EmployeeCreatedText_xpath = "//div[contains(text(),'Employee created successfully')]"

    def __init__(self, driver):
        self.driver = driver

    def clickEmployeesModule(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_employeesModule_xpath)))
        element.click()

    def Text_EmployeeCreatedSuccessful(self):
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.Verify_EmployeeCreatedText_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def clickAddButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Add_xpath)))
        element.click()

    def clickCountryDD(self):
        time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.DD_CountryDD_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH, self.DD_CountryDD_xpath).click()

    def clickActive(self):
        self.driver.find_element(By.XPATH, self.button_Active_xpath).click()

    def clickNewButton(self):
        self.driver.find_element(By.XPATH, self.button_New_xpath).click()


    def setDivisionName(self, searchField):
        self.driver.find_element(By.XPATH, self.text_Division_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_Division_xpath).send_keys(searchField)
    def clickAddDeptButton(self):
        time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.button_AddDept_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(1)

    def clickDoneAddDept(self):
        self.driver.find_element(By.XPATH, self.button_DoneAddDept_xpath).click()

    def clickAddDivisionButton(self):
        self.driver.find_element(By.XPATH, self.button_AddDivision_xpath).click()

    def clickAddDesignation(self):
        self.driver.find_element(By.XPATH, self.button_AddDesignation_xpath).click()

    def setActiveSearchField(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_activeSearchField_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_activeSearchField_xpath).send_keys(activeSearchField)

    def setFullname(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_fullname_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_fullname_xpath).send_keys(activeSearchField)

    def setEmail(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(activeSearchField)

    def setPersonalEmail(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_personalEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_personalEmail_xpath).send_keys(activeSearchField)

    def setPhoneNumber(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_phoneNumber_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_phoneNumber_xpath).send_keys(activeSearchField)

    def setEmpId(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_empId_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_empId_xpath).send_keys(activeSearchField)

