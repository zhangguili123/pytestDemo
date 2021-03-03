
import requests

from test_request.api.base import Base


class Member(Base):
    # 读取成员
    def readUser(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return  self.send("get",url)
        #return  r.json()

    # 创建成员
    def createUser(self,userid:str,name:str,mobile:str,position:list,**kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid":userid,
            "name": name,
            "mobile": mobile,
            "department": position,
        }
        body.update(kwargs)
        return  self.send("post",url, json=body)
        #return rs.json()

    # 更新成员
    def updateUser(self,userid:str,name:str,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid":userid,
            "name": name
        }
        body.update(kwargs)
        return self.send("post",url, json=body)
        #return  r.json()

    # 删除成员
    def deleteUser(self,userid:str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return  self.send("get",url=url)
        #return  r.json()





