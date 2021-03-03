import  requests

def test_getToken():
    #获取token
     url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe85214dfdfa6e02c&corpsecret=nfkVIggtxX8VMDUuB634Y9cJxzzftfghCiyx9sT2GhI"
     rs=requests.get(url=url)
     js = rs.json()
     token = js['access_token']
     return token
#读取成员
def test_readUser():
    token = test_getToken()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ZhangGuiLi"
    r = requests.get(url=url)
    print(r.json())

#测试添加成员并验证成员是否已添加
def test_addUser():
     token=test_getToken()
     # 清理数据
     url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan0205"
     r = requests.get(url=url)
     print(r.json())
     url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
     body= {
         "userid": "zhangsan0205",
         "name": "张三啊",
         "mobile": "+86 13800000900",
         "department": [1],
         }
     rs = requests.post(url=url,json=body)
     print(rs.json())
     #读取成员
     url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ZhangGuiLi"
     r = requests.get(url=url)
     print(r.json())
#更新成员
def test_updateUser():
    token=test_getToken()
    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "zhangsan0205",
        "name": "张三哈哈",
        "mobile": "+86 13800000900",
        "department": [1],
    }
    r=requests.post(url,json=body)
    print(r.json())
#测试删除成员
def test_deleteUser():
    token=test_getToken()
    #数据准备
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "zhangsan0205",
        "name": "张三啊",
        "mobile": "+86 13800000900",
        "department": [1],
    }
    rs = requests.post(url=url, json=body)
    print(rs.json())
    #删除

    url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsan0205"
    r=requests.get(url=url)
    print(r.json())
    # 读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=ZhangGuiLi"
    r = requests.get(url=url)
    print(r.json())





