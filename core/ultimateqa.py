import time

from pageobjects.ultimateqaFifthPage import UltimateqaPage5
from pageobjects.ultimateqaFourthPage import UltimateqaPage4
from pageobjects.ultimateqaLastPage import UltimateqaLastPage
from pageobjects.ultimateqaSecondPage import UltimateqaPage2
from pageobjects.ultimateqaThirdPage import UltimateqaPage3
from pageobjects.ultimateqafirstpage import UltimateqaPage
from pageobjects.ultimateqasixPage import UltimateqaPage6
from utils.browser import Browser
import random
browser = Browser("https://ultimateqa.com/automation")
browser.launch()
driver = browser.driver
ultimateqa = UltimateqaPage(driver)
ultimateqa.clickOnCourses()
ultimateqa2 = UltimateqaPage2(driver)
ultimateqa2.search()
ultimateqa3 = UltimateqaPage3(driver)
ultimateqa3.clickOnASpecificCourses()
ultimateqa4 = UltimateqaPage4(driver)
ultimateqa4.clickOnEFF()
ultimateqa5 = UltimateqaPage5(driver)
ultimateqa5.enterEmail(f'test{random.randint(1000, 100000)}@gmail.com')
ultimateqa5.enterFirstName("raina")
ultimateqa5.enterLastName("azad")
ultimateqa5.tickCheckbox()
ultimateqa5.submit()
ultimateqa6 = UltimateqaPage6(driver)
ultimateqa6.enterNewPassword(f"raina{random.randint(100,999)}")
ultimateqa6.submit()
ultimateqalast = UltimateqaLastPage(driver)
ultimateqalast.playTheVideo()
time.sleep(10)
driver.close()
