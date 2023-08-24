from selenium.webdriver.common.by import By

class LoginPage:
    textbox_clinic_xpath = "//*[@id='clinic']/span/input"
    textbox_username_xpath = "//*[@id='username']/span/input"
    textbox_password_xpath = "//*[@id='password']/span/input"
    btn_login_xpath = "//*[text() = 'Login']"
    invalid_msg_xpath = "/html/body/mtab-login/div[1]/div[2]/div/div/form/div[2]/span"

    def __init__(self, driver):
        self.driver = driver

    def set_clinic(self, clinic):
        self.driver.find_element(By.XPATH, self.textbox_clinic_xpath).send_keys(clinic)

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def verify_valid_credentials(self):
        str1 = self.driver.find_element(By.XPATH, "/html/body").text
        if "Invalid username or password" in str1:
            print("string>>>>>>>>>>>>>>>")
            return False

        else:
            return True


