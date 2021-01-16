from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
from test_po.page.add_member_page import AddMemberPage
from test_po.page.partMent_page import AddPartMentPage


class MainPage(BasePage):
    def goto_connect(self):
       pass
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return  AddMemberPage(self.driver)
    def goto_add_partment(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return  AddPartMentPage(self.driver)
