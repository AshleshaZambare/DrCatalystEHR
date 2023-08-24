import logging
import time

from PageObjects import LoginPage
from utilities.ReadConfig import Readconfig
from utilities import XLUtils
from utilities.Logger import LogGenerator

class TestLogin:
    clinic = "asbc"
    username = "ashlesha"
    password = "Neha@7276"
    log = LogGenerator.loggen()

    #Read from config file
    #clinic = Readconfig.Getclinic()
    #username = Readconfig.GetUsername()
    #password = Readconfig.Getpassword()

    #read from xl file
    # file = ".//testData//login_data.xlsx"
    # clinic = XLUtils.Read_Data(file, "Sheet1", 2, 1)
    # username = XLUtils.Read_Data(file, "Sheet1", 2, 2)
    # password = XLUtils.Read_Data(file, "Sheet1", 2, 3)

    def test_login(self, setup):
        #parameterization - pass (login_credentials - argument) to the test_login function for parameterization
        #self.clinic = login_credentials[0]
        #self.username = login_credentials[1]
        #self.password = login_credentials[2]

        self.log.info("------------------------- Starting test login-----------------------------")
        self.log.info("---------------------opening the browser ----------------------------")
        self.driver = setup
        self.lp = LoginPage.LoginPage(self.driver)
        self.log.info("--------------Entering clinic -------------------------------")
        self.lp.set_clinic(self.clinic)
        self.log.info("-------------entering username ------------------------")
        self.lp.set_username(self.username)
        self.log.info("----------------entering password ---------------------")
        self.lp.set_password(self.password)
        self.log.info("-------------Click on Login Button -----------------------")
        self.lp.click_login()
        time.sleep(5)

        if self.lp.verify_valid_credentials():
            self.log.info("---------Testcase Login Passed ---------------")
            self.log.info("-------------------Taking Screenshot ------------------")
            self.driver.save_screenshot(".//Screenshots//login_test.PNG")
            assert True
        else:
            self.log.info("---------Testcase Login Failed ---------------")
            self.log.info("-------------Taking screenshot -------------------------")
            self.driver.save_screenshot(".//Screenshots//login_test.PNG")
            assert False

        self.log.info("-----------Test Login Completed----------------")
        self.driver.close()


