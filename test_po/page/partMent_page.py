from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
from test_po.page.connect_page import connectPage


class AddPartMentPage(BasePage):
     def addPart(self):
         self.find(By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [name='name']").send_keys("部门1")
         self.find(By.CSS_SELECTOR, ".js_parent_party_name").click()
         self.find(By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [id='1688851974906588_anchor']").click()
         #self.find(By.XPATH,"//*[@id='__dialog__MNDialog__.]/div/div[3]/a[1]").click()
         self.driver.find_element(By.CSS_SELECTOR, '[id=__dialog__MNDialog__] div>div>a:nth-child(1)').click()
         return connectPage(self.driver)
