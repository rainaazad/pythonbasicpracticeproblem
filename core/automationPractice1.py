from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
driver.find_element_by_css_selector("input[name='search_query']").send_keys("shirt")
driver.find_element_by_css_selector("button[name='submit_search']").click()
# driver.find_element_by_css_selector("select[id='selectProductSort']").click()
driver.implicitly_wait(10)
a = ActionChains(driver)
m = driver.find_element_by_css_selector("div[class='product-container']")
a.move_to_element(m).perform()
driver.find_element_by_xpath("//span[text()='Add to cart']").click()
driver.find_element_by_css_selector("a[title='Proceed to checkout']").click()
driver.find_element_by_xpath("(//a[@title='Proceed to checkout'])[2]").click()
# driver.find_element_by_css_selector("a[title='View my shopping cart']").click()
# driver.find_element_by_css_selector("input[name='email_create']").send_keys("rainaazad@gmail.com")
# driver.find_element_by_css_selector("button[id='SubmitCreate']").click()
driver.find_element_by_xpath("//input[@id='email']").send_keys("rainaazad@gmail.com")
driver.find_element_by_xpath("//input[@id='passwd']").send_keys("#raina1")
driver.find_element_by_css_selector("button[id='SubmitLogin']").click()
# driver.find_element_by_xpath("//a[@title='View my shopping cart']").click()
# driver.find_element_by_css_selector("a[title='Check out']").click()
driver.find_element_by_xpath("//button[@name='processAddress']").click()
#driver.find_element_by_xpath("//p[@class='checkbox']").click()
# try:
#     driver.find_element_by_css_selector("a[title='Close']").click()
# except NoSuchElementException:
#     print("element does not exist")
# try:
#     driver.find_element_by_css_selector("a[title='Close']").click()
# except NoSuchElementException:
#     print("element does not exist")
driver.find_element_by_css_selector("input[type='checkbox']").click()
driver.find_element_by_xpath("//button[@name='processCarrier']").click()
price = driver.find_element_by_css_selector("span[id='total_price']").text
print("your total price is", price)
driver.find_element_by_css_selector("a[class='cheque']").click()
driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
success = driver.find_element_by_css_selector("p[class='alert alert-success']").text

assert "complete" in success

driver.close()


