from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def launch(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
