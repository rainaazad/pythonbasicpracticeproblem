from selenium.webdriver.common.by import By

from core.automation_utils import wait_for_element_to_be_visible


class LogInPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@id='loginusername']")
    password = (By.ID, "loginpassword")
    submit = (By.CSS_SELECTOR, "button[onclick='logIn()']")
    loginLink = (By.ID, "login2")

    def loginToApplication(self, username, password):
        wait_for_element_to_be_visible(self.driver, LogInPage.username)
        self.driver.find_element(*LogInPage.username).send_keys(username)
        self.driver.find_element(*LogInPage.password).send_keys(password)
        wait_for_element_to_be_visible(self.driver, LogInPage.submit)
        self.driver.find_element(*LogInPage.submit).click()

    def clickLoginLink(self):
        self.driver.find_element(*LogInPage.loginLink).click()
