from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element_to_be_visible(driver, locator):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(locator))