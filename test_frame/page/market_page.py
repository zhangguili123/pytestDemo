from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage
from test_frame.page.serach_page import SerachPage


class MarketPage(BasePage):
   def goto_search(self):
       self.find_and_click((MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
       #self.driver.find_element(MobileBy.XPATH, '//*[@resource="com.xueqiu.android:id/action_search"]').click()
       return SerachPage(self.driver)