import  pytest
import yaml

from pythoncode.calculator import Calcultor


def get_data_work():
    with open("./datawork.yaml") as  f:
        datas = yaml.safe_load(f)
        add_datas = datas["add_datas"]
        sub_datas = datas["sub_datas"]
        mul_datas = datas["mul_datas"]
        div_datas = datas["div_datas"]
        submyids = datas["submyids"]
        addmyids = datas["addmyids"]
        mulmyids = datas["mulmyids"]
        devmyids = datas["devmyids"]
        return [add_datas, sub_datas, mul_datas, div_datas, addmyids,submyids,mulmyids,devmyids]
class TestCalc:
    @classmethod
    def setup_class(self):
        print("开始全部计算")
    @classmethod
    def teardown_class(self):
        print("结束全部计算")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def setup_class(self):
        self.calc=Calcultor()
    #加法

    @pytest.mark.parametrize("a,b,expect",get_data_work()[0],ids=get_data_work()[4])
    def test_add(self,a,b,expect):
        result=self.calc.add(a,b)
        assert  result==expect

    #减法
    @pytest.mark.parametrize("a,b,expect", get_data_work()[1], ids=get_data_work()[5])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    #除法
    @pytest.mark.parametrize("a,b,expect", get_data_work()[2], ids=get_data_work()[6])
    def test_mul(self, a, b, expect):
        try:
           result = self.calc.mul(a, b)
           assert result == expect
        except:
            print("0 不能作为除数")
    #乘法
    @pytest.mark.parametrize("a,b,expect", get_data_work()[3], ids=get_data_work()[7])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect



