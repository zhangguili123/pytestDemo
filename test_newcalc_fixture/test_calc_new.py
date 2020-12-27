import  pytest
from pythoncode.calculator import Calcultor
from test_newcalc_fixture.conftest import get_data_work
class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calcultor()
    #加法
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect", get_data_work()[0],ids= get_data_work()[4])
    @pytest.mark.usefixtures("star_end")
    def test_add(self,a,b,expect):
       # result=self.calc.add(a,b)
        result = self.calc.add(a, b)
        assert  result==expect
    # 除法
    @pytest.mark.usefixtures("star_end")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expect", get_data_work()[2], ids=get_data_work()[6])
    def test_mul(self, a, b, expect):
        try:
            result = self.calc.mul(a, b)
            assert result == expect
        except:
            print("0 不能作为除数")
    #乘法
    @pytest.mark.usefixtures("star_end")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expect", get_data_work()[3], ids=get_data_work()[7])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
    #减法
    @pytest.mark.usefixtures("star_end")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expect", get_data_work()[1], ids=get_data_work()[5])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect



