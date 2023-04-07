from selenium.webdriver.common.by import By


class LoginPge:
    Dict = {"id_username": 'Email', "id_password": "Password",
            "Xpath_LoginBtn": '//button[@class="button-1 login-button"]',
            "Click_Cust": "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a",
            "Click_SubCust": "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"}

    def __init__(self, driver):
        self.driver = driver

    def SetUsername(self, username):
        self.driver.find_element(By.ID, self.Dict["id_username"]).clear()
        self.driver.find_element(By.ID, self.Dict["id_username"]).send_keys(username)

    def Setpassword(self, password):
        self.driver.find_element(By.ID, self.Dict["id_password"]).clear()
        self.driver.find_element(By.ID, self.Dict["id_password"]).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.Dict["Xpath_LoginBtn"]).click()

    def ClickOnCust(self):
        self.driver.find_element(By.XPATH, self.Dict['Click_Cust']).click()

    def ClickOnSubCust(self):
        self.driver.find_element(By.XPATH, self.Dict["Click_SubCust"]).click()
