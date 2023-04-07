from Dictionary.Selenium_Class.Login_page import LoginPge
from selenium import webdriver
import time

class TestLogin:

    Dict = {"username": 'admin@yourstore.com', "password": "admin",
            "Url": "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"}


    def test_homepageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.Dict['Url'])
        time.sleep(6)
        self.driver.maximize_window()
        get_title = self.driver.title
        self.driver.close()
        if get_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.Dict['Url'])
        time.sleep(6)
        self.driver.maximize_window()
        self.ip = LoginPge(self.driver)
        self.ip.SetUsername(self.Dict["username"])
        time.sleep(5)
        self.ip.Setpassword(self.Dict['password'])
        time.sleep(5)
        self.ip.Click_Login()
        time.sleep(5)
        self.ip.ClickOnCust()
        time.sleep(3)
        self.ip.ClickOnSubCust()
        act_title = self.driver.title
        if act_title == "Customers / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            assert False

