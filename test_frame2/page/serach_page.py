import yaml
from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage


class SerachPage(BasePage):
    def search(self):
         self.find_step_run("../page/search_page.yaml","search")
         # self.send((MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']"),"阿里巴巴")
         # self.find_and_click((MobileBy.XPATH,"//*[@text='阿里巴巴-SW']"))
         return  True


