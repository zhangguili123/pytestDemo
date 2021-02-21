import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.find_step_run("../page/main_page.yaml","goto_market")
        # self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        # self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)
    def goto_me(self):
        self.find_step_run("../page/main_page.yaml","goto_me")
        # self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        # self.find_and_click((MobileBy.XPATH, "//*[@text='行情']"))
        #return MarketPage(self.driver)
