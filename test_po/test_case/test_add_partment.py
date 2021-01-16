from test_po.page.main_page import MainPage


class Test_addParment():
    def setup_class(self):
        self.main = MainPage()
    def test_addParment(self):
        result =self.main.goto_add_partment().addPart().get_newPart()
        assert "部门1" in result