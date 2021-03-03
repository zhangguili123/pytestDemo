import requests


class Base:
    def __init__(self):
        # 获取token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe85214dfdfa6e02c&corpsecret=nfkVIggtxX8VMDUuB634Y9cJxzzftfghCiyx9sT2GhI"
        r = requests.get(url).json()
        self.token = r['access_token']
        self.s=requests.Session()
        self.s.params= {'access_token':self.token}
    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs).json()