##Page Object Model for LogIn
#POM is used here for better code organization, maintainability, and reusability, even its small part of a project

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()



