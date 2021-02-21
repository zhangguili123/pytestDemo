from time import sleep

from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
class connectPage(BasePage):
    def add_department(self):
        pass
    def add_connet(self):
        pass

    #返回通讯录页面的人员信息
    #".member_colRight_memberTable_td:nth-child(2)"
    def get_list(self):
        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list=[]
        for name_webelement in name_webelement_list:
            name_list.append(name_webelement.text)
        return  name_list

    def get_newPart(self):
       # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        #ul=self.find(By.ID,"1688851974906588_anchor")
        #newparts=self.find(By.XPATH,"//*[@id='js_contacts51']/div/div[1]/div/div[2]/div[2]/ul/li")
        sleep(3)
        #newparts = self.driver.find_elements_by_xpath('//ul[@role="group"] //li')
        newparts = self.driver.find_elements_by_xpath("//*[@id='js_contacts12']/div/div[1]/div/div[2]/div[2]/ul/li")
        part_list=[]
        for newpart in  newparts:
            newpart = newpart.text.strip()
            part_list.append(newpart)
        return  part_list




