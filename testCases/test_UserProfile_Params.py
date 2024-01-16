import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig


class Test_User_Profile_Params:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()

    # def test_UserRegistration_params004(self, setup):
    #     self.driver = setup
    #     # 1 Browser Open
    #     # self.driver = webdriver.Firefox()
    #
    #     self.ur = UserProfile_Class(self.driver)
    #     # 2 Go to registration url
    #     self.driver.get(self.RegistrationUrl)
    #
    #     # 3 Enter Name
    #     # driver.find_element(By.ID, 'name').send_keys("Rohit")
    #     self.ur.Enter_Name("Rohit")
    #
    #     # 4 Enter EMail Id
    #     # self.driver.find_element(By.ID, 'email').send_keys("Rohit3442@credence.in")
    #     self.ur.Enter_Email("TestUser101@credence.in")
    #
    #     # 5 Enter Password
    #     # self.driver.find_element(By.ID, 'password').send_keys("rohit@123")
    #     self.ur.Enter_Password("Test123")
    #
    #     # 6 Enter Confirm Password
    #     # self.driver.find_element(By.ID, "password-confirm").send_keys("rohit@123")
    #     self.ur.Enter_ConfirmPassword("Test123")
    #
    #     # 7 Click on Register button
    #     # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #
    #     self.ur.Click_Login_Or_RegisterButton()
    #
    #     # 7 Validate Registration
    #     # try:
    #     #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
    #     #     print("Registration Pass")
    #     #     assert True
    #     # except:
    #     #     print("Registration Fail")
    #     #     assert False
    #
    #     if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
    #         self.driver.save_screenshot(
    #             "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Registration_Pass.png")
    #         # self.driver.close()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Registration_Fail.png")
    #         # self.driver.close()
    #         assert False

    def test_UserLogin_Params_005(self, setup, getDataForLogin):
        self.driver = setup
        self.driver.get(self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)
        self.ur.Enter_Email(getDataForLogin[0])
        print("Username-->" + getDataForLogin[0])
        self.ur.Enter_Password(getDataForLogin[1])
        print("Password-->" + getDataForLogin[1])
        self.ur.Click_Login_Or_RegisterButton()
        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")

                assert True
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")
                assert False

        else:# Login Fail
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")

                assert False
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Pass.png")
                assert True

            self.driver.save_screenshot(
                "C:\\Users\\HP\\Desktop\\Python revision Jan 24\\Pytest_Credkart\\Screenshots\\Login_Fail.png")


# pytest -v --html=HTMLReports/Edge_Report.html --browser chrome -n=5 --alluredir="C:\Users\HP\Desktop\Python revision Jan 24\Pytest_Credkart\AllureReports"
# allure serve "folder Path"


#

# config -- > url, login id pass
# Logs
# Data Driven Test Case
