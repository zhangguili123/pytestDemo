import pytest
import yaml
from pythoncode.calculator import Calcultor
import  os
yaml_file_path=os.path.dirname(__file__)+"./datawork2.yaml"
@pytest.fixture(scope="session")
def connectDB():
    print("sub连接DB")
    yield
    print("sub断开DB")
@pytest.fixture(scope="class")
def get_calc():
    #print("----开始计算----")
    #print("获取计算器实例")
    calc = Calcultor()
    return calc

def get_data_work():
    with open("./datawork2.yaml") as  f:
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
@pytest.fixture(scope="module")
def star_end():
    print("---------开始计算----------------\n")
    yield
    print("\n------------结束计算------------")



