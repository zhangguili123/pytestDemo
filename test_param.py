import pytest

def add_fun(a,b):
    return  a+b
@pytest.mark.parametrize("a,b,expected",[(1,1,2),(2,3,5),(3,3,6)],ids=["a","b","c"])
def test_add(a,b,expected):
    assert  add_fun(a,b)== expected