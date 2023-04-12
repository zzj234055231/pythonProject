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
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('baidu')
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
        time.sleep(1)
        # 滚动到页面底部
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        time.sleep(3)
        # 点击下一页
        self.driver.find_element(By.CSS_SELECTOR, '#page > div > a.n').click()
        time.sleep(3)
