import pytest
import yaml

from test_appium.page.app import App


def get_data():
    with open('../data/data.yaml', encoding="UTF-8") as f:
        data = yaml.safe_load(f)
        add_data = data['add']
        return add_data

class TestConnect():
    def setup(self):
        self.app=App();
    def setup(self):
        self.app = App()
        self.main = self.app.start().gotoMain()

    def teardown(self):
        self.app.stop()



    @pytest.mark.parametrize("name,gender,phone",get_data())

    def test_add_contact(self,name,gender,phone):
        # name = 'zhangsan4'
        # gender = '男'
        # phone = '19800000004'
        toast = self.main.click_addresslist().add_member().addmember_Byhand(). \
            edit_name(name).edit_gender(gender).edit_phonenum(phone).click_save().go_toast()
        assert toast == "添加成功"



