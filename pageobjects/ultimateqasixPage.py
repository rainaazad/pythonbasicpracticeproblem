import time

from selenium.webdriver.common.by import By

from core.automation_utils import wait_for_element_to_be_visible


class UltimateqaPage6:

    def __init__(self, driver):
        self.driver = driver

    newPassword = (By.CSS_SELECTOR, "input[type='password']")
    submitB = (By.CSS_SELECTOR, "input[type='submit']")

    def enterNewPassword(self, password):
        # wait_for_element_to_be_visible(self.driver, UltimateqaPage6.newPassword)
        time.sleep(5)
        self.driver.find_element(*UltimateqaPage6.newPassword).send_keys(password)

    def submit(self):
        self.driver.find_element(*UltimateqaPage6.submitB).click()
