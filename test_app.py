from time import sleep
from selenium.webdriver.common.by import By
from appium import webdriver


class TestAppium:

    def setup(self):
        desire_caps = {
            'platformName': 'android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.android.calculator2',
            'appActivity': 'Calculator t13'
            }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_app(self):
        self.driver.find_element(By.ID, 'com.android.calculator2:id/digit_7').click()
        self.driver.find_element(By.ID, 'com.android.calculator2:id/op_add').click()
        self.driver.find_element(By.ID, 'com.android.calculator2:id/digit_7').click()
        self.driver.find_element(By.ID, 'com.android.calculator2:id/eq').click()
        sleep(3)
