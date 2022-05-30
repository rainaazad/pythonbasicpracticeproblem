from selenium.webdriver.common.by import By


class UltimateqaPage4:

    def __init__(self, driver):
        self.driver = driver

    enrollForFree = (By.XPATH, "//a[text()='Enroll for free']")


    def clickOnEFF(self):
        self.driver.find_element(*UltimateqaPage4.enrollForFree).click()
