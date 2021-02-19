from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage
from test_appium.page.connectedit_page import ConnectEditPage


class MemberByHandPage(BasePage):
  # def __init__(self, driver):
  #       self.driver = driver
    #点击手动添加
  def addmember_Byhand(self):
      #self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
      self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
      return  ConnectEditPage(self.driver)

  def go_toast(self):
      #ele = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
      ele=self.find_and_get_text((MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
      return  ele

