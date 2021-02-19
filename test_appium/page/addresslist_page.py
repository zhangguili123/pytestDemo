#点击添加成员
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.memberbyhand_page import MemberByHandPage


class addressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.scroll_find_click('添加成员')
        return  MemberByHandPage(self.driver)
