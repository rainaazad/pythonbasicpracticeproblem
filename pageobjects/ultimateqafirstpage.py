from selenium.webdriver.common.by import By


class UltimateqaPage:

    def __init__(self, driver):
        self.driver = driver

    course = (By.XPATH, "//a[text()='Courses']")
    def clickOnCourses(self):
        self.driver.find_element(*UltimateqaPage.course).click()

