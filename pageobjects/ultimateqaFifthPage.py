import time

from selenium.webdriver.common.by import By

from core.automation_utils import wait_for_element_to_be_visible


class UltimateqaPage5:

    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "input[type='email']")
    firstName = (By.CSS_SELECTOR, "input[name='firstName']")
    lastName = (By.CSS_SELECTOR, "input[name='lastName']")
    checkbox = (By.XPATH, "//div[@class='terms-and-privacy']//input")
    signIn = (By.CSS_SELECTOR, "button[type='submit']")  # (//label[contains(text(),'I agree to ')]//preceding::input)[4]

    def enterEmail(self, email):
        wait_for_element_to_be_visible(self.driver, UltimateqaPage5.email)
        self.driver.find_element(*UltimateqaPage5.email).send_keys(email)

    def enterFirstName(self, first_name):
        self.driver.find_element(*UltimateqaPage5.firstName).send_keys(first_name)

    def enterLastName(self, last_name):
        self.driver.find_element(*UltimateqaPage5.lastName).send_keys(last_name)

    def tickCheckbox(self):
        # wait_for_element_to_be_visible(self.driver, UltimateqaPage5.checkbox)
        # time.sleep(5)
        element = self.driver.find_element(*UltimateqaPage5.checkbox)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        self.driver.find_element(*UltimateqaPage5.signIn).click()


