import yaml
from appium.webdriver.common.mobileby import MobileBy


def handblack(fun):
    def run(*args, **kwargs):
        self=args[0]
        with open("black.yaml","r",encoding="utf-8") as f:
            blacklist=yaml.load(f)
        #blacklist = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            #遍历黑名单
            for black in blacklist:
                #黑名单元素存在
                  eles = self.driver.find_elements(*black)
                  if len(eles) > 0:
                      #通过点击的方式 关闭黑名单
                      eles[0].click()
                      return  fun(*args, **kwargs)

        raise  e

    return  run
