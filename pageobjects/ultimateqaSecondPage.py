from selenium.webdriver.common.by import By


class UltimateqaPage2:

    def __init__(self, driver):
        self.driver = driver

    searchBox = (By.CSS_SELECTOR, "input[type='search']")

    def search(self):
        self.driver.find_element(*UltimateqaPage2.searchBox).send_keys("selenium")
        self.driver.find_element(*UltimateqaPage2.searchBox).submit()


