from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_frame.handblack import  handle_black


class BasePage():
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
    @handle_black
    def find(self,locator):
          return  self.driver.find_element(*locator)


    def find2(self,locator):
       # sleep(3)
        blacklist=[(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
       # sleep(2)
        #self.find_and_click((By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]'))
        #捕获异常（元素没找到）
        try:
          result= self.driver.find_element(*locator)
          return  result
        except Exception as e:
            #遍历黑名单
            for black in blacklist:
                #黑名单元素存在
                  eles = self.driver.find_elements(*black)
                  if len(eles) > 0:
                      #通过点击的方式 关闭黑名单
                      eles[0].click()
                      return  self.find(locator)

        raise  e
    #复制老师的find代码
    def find1(self,locator):
        #sleep(2)
        black_lists=[(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        #self.find_and_click((By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]'))
        #捕获异常（元素没找到）
        try:
            # 如果元素找到，就返回
            result = self.driver.find_element(*locator)
            return result
        except Exception as e:
            # 遍历黑名单
            for black in black_lists:
                # 如果发现黑名单中的元素存在
                eles = self.driver.find_elements(*black)
                # 对黑名单元素进行处理
                if len(eles) > 0:
                    # 通过点击的方式，关闭弹窗
                    eles[0].click()
                    # 再次查找
                    return self.find(locator)
            raise e

    def find_and_click(self, locator):
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


