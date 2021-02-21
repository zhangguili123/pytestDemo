from time import sleep

import yaml
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
    def find_and_click(self, locator):
        self.find(locator).click()
    def send(self,locator,context):
        self.find(locator).send_keys(context)

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
    #po下多个操作
    def find_step_run(self,pagepath,operation):
        with open(pagepath, 'r', encoding="utf-8") as f:
            data = yaml.load(f)
            steps=data[operation]
        for step in steps:
            action = step['action']
            if action == 'find_and_click':
                self.find_and_click(step['locator'])
            elif action == 'send':
                self.send(step['locator'], step['context'])



