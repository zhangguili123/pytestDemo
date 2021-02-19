from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
    def find(self,locator):
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
         self.find(locator).click()

    def find_and_sendkey(self,locator,text):
          self.find(locator).send_keys(text)
    def scroll_find_click(self,text):
        # 添加成员 滑动查找
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)
    def find_and_get_text(self,locator):
        return  self.find(locator).text


