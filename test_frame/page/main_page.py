from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        #self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']"))
        self.find_and_click((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']"))
        self.find_and_click((MobileBy.XPATH,"//*[@text='行情']"))
        return  MarketPage(self.driver)