import pytest

from test_request.api.member import Member


class TestMember:
    def setup(self):
        self.Member=Member();
    @pytest.mark.parametrize("userid,mobile",[("lisi21","19800000011"),
                                              ("lisi22","19800000012"),
                                              ("lisi32","19800000013")])
    def test_addMember(self,userid,mobile):
        name="张三测试2"
        position=[1]
        #数据清理
        self.Member.deleteUser(userid)
        #创建成员
        r=self.Member.createUser(userid=userid,name=name,mobile=mobile,position=position)
        assert  r.get("errcode")==0
        #查询
        r=self.Member.readUser(userid=userid)
        assert  r.get("name","userid 添加失败")==name




