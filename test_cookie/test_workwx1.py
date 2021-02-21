from time import sleep

import pytest
from  selenium import  webdriver
import  json

class Test_wx():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "localhost:9333"
        #使用cookie
        #self.driver = webdriver.Chrome()
        #浏览器复用
        self.driver = webdriver.Chrome(options=chrome_args)

    # pytest.mark.skip
    # def tear_down(self):
    #     self.driver.quit()
   #以文件流的形式写cookie
    #pytest.mark.skip
    def test_wcookies(self):
        cookies=self.driver.get_cookies()
        #以文件流的形式打开文件
        with open("cookies.json","w") as  f:
            #存储cookie到cookies.json
            json.dump(cookies,f)
    #读取cookies
    #pytest.mark.skip
    def test_rcookies(self):
        with open("cookies.json","r") as f:
            #读取cookie
            cookies=json.load(f)
            print(cookies)
   #作业
    # 使用 cookie，实现企业微信的点击客户联系
    #pytest.mark.skip
    def test_usecookis(self):
        self.driver.get("https://work.weixin.qq.com")
        with open("cookies.json","r") as  f:
            cookies=json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
        self.driver.find_element_by_id("menu_customer").click()

    #使用浏览器复用，实现企业微信的点击客户联系
    #pytest.mark.skip
    def test_workwx(self):
        self.driver.get("https://work.weixin.qq.com")
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
        # self.driver.find_element_by_xpath("//*[@id='menu_customer']/span").click()
        self.driver.find_element_by_id("menu_customer").click()
        #self.driver.close()