from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class TestWebdriver:

    def setup(self):
        self.driver = webdriver.Edge()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_web(self):
        self.driver.find_element(By.ID, 'kw').send_keys('baidu')
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(3)
