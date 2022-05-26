import time

from selenium.webdriver.common.by import By

from core.automation_utils import wait_for_element_to_be_visible


class ProductsBuying:
    def __init__(self, driver):
        self.driver = driver

    nameOfUser = (By.ID, "nameofuser")
    laptop = (By.XPATH, "//a[text()='Laptops']")
    products = (By.XPATH, "//a[@class='hrefch']")
    __addToCart = (By.XPATH, "//a[text()='Add to cart']")

    def getUsername(self):
        wait_for_element_to_be_visible(self.driver, ProductsBuying.nameOfUser)

        print(self.driver.find_element(*ProductsBuying.nameOfUser).text)

    def selectLaptop(self):
        self.driver.find_element(*ProductsBuying.laptop).click()
        time.sleep(3)
        products = self.driver.find_elements(*ProductsBuying.products)
        for product in products:
            product_name = product.text
            # print(product_name)
            if product_name == "MacBook Pro":
                laptop = product_name
                product.click()
                return laptop

    def addToCart(self):
        wait_for_element_to_be_visible(self.driver, ProductsBuying.__addToCart)
        self.driver.find_element(*ProductsBuying.__addToCart).click()
