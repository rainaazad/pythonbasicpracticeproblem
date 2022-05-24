from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()
driver.find_element_by_css_selector("input[title='Search for products, brands and more']").send_keys("macbook")
driver.find_element_by_css_selector("button[type='submit']").click()
driver.implicitly_wait(5)

checkboxes = driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")

print(len(checkboxes))
count = 0

for ele in checkboxes:
    if count == 2:
        break
    count = count + 1
    ele.click()

driver.find_element_by_xpath("//span[text()='COMPARE']").click()
driver.find_element_by_xpath("//span[@class='_1JecnH']").click()
Product1 = driver.find_element_by_xpath("//div[text()='₹1,02,990']").text
Product2 = driver.find_element_by_xpath("//div[text()='₹92,900']").text
if Product1 > Product2:
    print("Product1 is a better product.")
else:
    print("Product2 is a better product.")

driver.close()
