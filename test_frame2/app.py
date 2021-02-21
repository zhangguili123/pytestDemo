#存放对app的操作 页 启动app  关闭app  重启app  进入首页
from test_appium.page.base_page import BasePage
from appium import  webdriver

from test_frame.page.main_page import MainPage


class App(BasePage):
    def start(self):
         if self.driver==None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            # 不清空本地缓存，启动app
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间为0秒
            caps['settings[waitForIdleTimeout]'] = 1
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
         else:
             self.driver.launch_app()#自动调用已设置的app
         return  self
    def restart(self):
        self.driver.quit()
        self.start()
        return  self
    def stop(self):
        self.driver.quit()
        return  self
    def gotoMain(self)->MainPage:
        return  MainPage(self.driver)