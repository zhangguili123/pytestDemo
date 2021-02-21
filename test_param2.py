import pytest


@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[2,3])
def test_foo1(a,b):
    print("a->%s,b->%s"%(a,b))
