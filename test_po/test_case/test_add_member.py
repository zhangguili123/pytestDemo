from test_po.page.main_page import MainPage



class Test_AddMember():
    def setup_class(self):
        self.main = MainPage()
    def test_addmember(self):
        #Alt+回车可以快捷导入
        #1首页跳转到添加成员页面 2、添加成员 3、返回成员信息列表
        result=self.main.goto_add_member().add_member("13145212","13145212","13866668887").get_list()
        assert "13145212" in result
    def test_addmemberFail(self):
        #Alt+回车可以快捷导入
        #1首页跳转到添加成员页面 2、添加成员 3、返回成员信息列表
        result=self.main.goto_add_member().add_memnerFail("张贵丽2","13145212","19840858781").get_list()
        #result=self.main.goto_add_member().username
        assert "张贵丽2" not in result
