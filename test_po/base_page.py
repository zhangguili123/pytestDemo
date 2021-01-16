import json
from  selenium import  webdriver
from selenium.webdriver.remote.webdriver import WebDriver
class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self._cookielogin()
        else:
            self.driver=driver
        self.driver.implicitly_wait(3)
    # 使用 cookie，实现企业微信的点击客户联系
    def  _cookielogin(self):
        self.driver.get("https://work.weixin.qq.com")
        with open("../cookies.json","r") as  f:
            cookies=json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)





