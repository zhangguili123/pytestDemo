#点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslist_page import addressListPage
from test_appium.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def click_addresslist(self):
        #self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return   addressListPage(self.driver)



