from  selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestHs():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()


def test_test1(self):
    self.driver.get("https://ceshiren.com/c/9-category/82-category/82")
    self.driver.set_window_size(1218, 1026)
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) img")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element).perform()
    # element = self.driver.find_element(By.CSS_SELECTOR, "body")
    # actions = ActionChains(self.driver)
    # actions.move_to_element(element, 0, 0).perform()
    # self.driver.find_element(By.CSS_SELECTOR, "#ember83 > .main-link").click()
