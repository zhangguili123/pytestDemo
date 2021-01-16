from selenium.webdriver.common.by import By

from test_po.page.connect_page import connectPage
from test_po.base_page import BasePage

class AddMemberPage(BasePage):
    _username=(By.ID,"username")
    def add_member(self,name,acctid,phone):
        # 输入成员信息，点击保存
        self.find(By.ID,"username").send_keys(name)
        self.find(By.ID,"memberAdd_acctid").send_keys(acctid)
        self.find(By.ID,"memberAdd_phone").send_keys(phone)
        #self.driver.find_element_by_class_name(".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return  connectPage(self.driver)
    def add_memnerFail(self,name,acctid,phone):
        # 输入成员信息，点击保存
        # 输入成员信息，点击保存
        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        # self.driver.find_element_by_class_name(".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return connectPage(self.driver)


