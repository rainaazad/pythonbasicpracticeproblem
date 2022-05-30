from selenium.webdriver.common.by import By

from core.automation_utils import wait_for_element_to_be_visible


class UltimateqaLastPage:

    def __init__(self, driver):
        self.driver = driver

    playVideo = (By.CSS_SELECTOR, "button[title='Play Video']")

    def playTheVideo(self):
        wait_for_element_to_be_visible(self.driver, UltimateqaLastPage.playVideo)
        self.driver.find_element(*UltimateqaLastPage.playVideo).click()
