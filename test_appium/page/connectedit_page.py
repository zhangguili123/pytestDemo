from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage


class ConnectEditPage(BasePage):
     # def __init__(self, driver):
     #    self.driver = driver
    #编辑成员信息

     def edit_name(self,name):
         # 姓名
         self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
         #self.find_and_sendkey((MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText",name))
         return  self
     def edit_gender(self,gender):
         locator = (MobileBy.XPATH, "//*[@text='男']")
         ele = WebDriverWait(self.driver, 10).until(
             expected_conditions.element_to_be_clickable(locator))
         ele.click()
         #self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
         if gender == '女':
              self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
              #self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
         else:
             #self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
             self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
         return  self
     def edit_phonenum(self,phone):
         self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fwi").send_keys(phone)
         #self.find_and_sendkey((MobileBy.ID, "com.tencent.wework:id/fwi",phone))
         return  self
     def click_save(self):
         from test_appium.page.memberbyhand_page import MemberByHandPage
         self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
         #self.find_and_click((MobileBy.XPATH, "//*[@text='保存']"))
         return  MemberByHandPage(self.driver)