from appium import  webdriver

desire_cap={
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset":"true",#页面覆盖
  "dontStopAppOnReset":"true", #不停止运行APP
  "skipDeviceInitialization":"true" #跳过权限配置
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)
driver.implicitly_wait(10)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
driver.back()
driver.back()
driver.quit()
