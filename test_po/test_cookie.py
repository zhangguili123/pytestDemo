import json
import pytest
class Test_cookie():
    def test_writecookies(self):
        cookies=self.driver.get_cookies()
        #以文件流的形式打开文件
        with open("cookies.json","w") as  f:
            #存储cookie到cookies.json
            json.dump(cookies,f)
    #读取cookies
    pytest.mark.skip
    def test_readcookies(self):
        with open("cookies.json","r") as f:
            #读取cookie
            cookies=json.load(f)
            print(cookies)