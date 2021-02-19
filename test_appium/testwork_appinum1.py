from appium import  webdriver
from appium.webdriver.common.mobileby import MobileBy
class TestWprk:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存，启动app
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间为0秒
        caps['settings[waitForIdleTimeout]'] = 1
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def testadd_member(self):
        name='zhangguili'
        gender='女'
        phone=19800000000
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()
        #添加成员 滑动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        #姓名
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="男"]').click()
        if gender=='女':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fwi").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        ele=self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        assert  "添加成功"== ele




