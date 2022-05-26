from pageobjects.LoginPage import LogInPage
from pageobjects.Products import ProductsBuying
from utils.browser import Browser


browser = Browser("https://www.demoblaze.com/")
browser.launch()
driver = browser.driver

loginPage = LogInPage(driver)
loginPage.clickLoginLink()
loginPage.loginToApplication("Raina Azad", "#raina1")

productPage = ProductsBuying(driver)
productPage.getUsername()
laptop = productPage.selectLaptop()
print(laptop)
productPage.addToCart()

# alert = Alert(driver)
# try:
#     alert.accept()
# except:
#     alert.dismiss()
# print(f"{laptop} {alert.text}")

driver.close()
