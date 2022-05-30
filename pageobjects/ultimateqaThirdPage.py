from selenium.webdriver.common.by import By


class UltimateqaPage3:

    def __init__(self, driver):
        self.driver = driver

    seleniumCourses = (By.XPATH, "//li[@class='products__list-item']")

    def clickOnASpecificCourses(self):
        seleniumCourses = self.driver.find_elements(*UltimateqaPage3.seleniumCourses)
        for course in seleniumCourses:
            courseName = course.text
            # print(courseName)
            if ("WHAT ARE IMPLICIT AND EXPLICIT WAITS") in courseName:
                course.click()
                break

