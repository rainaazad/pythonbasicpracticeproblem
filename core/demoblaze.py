import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

from automation_utils import wait_for_element_to_be_visible

laptop = ""

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.find_element_by_id("login2").click()
driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@id='loginusername']").send_keys("Raina Azad")
driver.find_element_by_id("loginpassword").send_keys("#raina1")

wait_for_element_to_be_visible(driver,(By.CSS_SELECTOR, "button[onclick='logIn()']"))

driver.find_element_by_css_selector("button[onclick='logIn()']").click()
wait_for_element_to_be_visible(driver,(By.ID, "nameofuser"))

username = driver.find_element_by_id("nameofuser").text
print(f"User name {username}")

driver.find_element_by_xpath("//a[text()='Laptops']").click()  # for buying phone
time.sleep(4)
products = driver.find_elements_by_xpath("//a[@class='hrefch']")

for product in products:
    product_name = product.text
    print(product_name)
    if product_name == "MacBook Pro":
        laptop = product_name
        product.click()
        break

driver.find_element_by_xpath("//a[text()='Add to cart']").click()
# driver.implicitly_wait(5)
alert = Alert(driver)
try:
    alert.accept()
except:
    alert.dismiss()
print(f"{laptop} {alert.text}")

driver.close()