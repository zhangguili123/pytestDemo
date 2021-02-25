import  requests
from  requests.auth import  HTTPBasicAuth
def test_demo():
    url="https://httpbin.testing-studio.com/cookies"
    header={"Cookie":"hogwarts=school"}
    r=requests.get(url = url,headers = header)
    print(r.request.headers)
    print(r.headers)
def test_auth():
    #url="https://httpbin.testing-studio.com/basic-auth/aaa/111"
    requests.get(url =  "https://httpbin.testing-studio.com/basic-auth/aaa/111",
                 auth = HTTPBasicAuth("aaa","111"))


