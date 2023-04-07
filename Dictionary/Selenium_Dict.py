# import data as data
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Dict = {"username": 'admin@yourstore.com', "Password": "admin"}
driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
Username_field = driver.find_element(By.ID, "Email")
Username_field.clear()
time.sleep(5)
Username_field.send_keys(Dict['username'])
time.sleep(5)
Password_field = driver.find_element(By.ID, "Password")
Password_field.clear()
time.sleep(3)
Password_field.send_keys(["Password"])
Password_field.send_keys(Dict["Password"])
Login_Btn = driver.find_element(By.XPATH, '//button[@class="button-1 login-button"]')
Login_Btn.click()
time.sleep(10)
driver.close()
