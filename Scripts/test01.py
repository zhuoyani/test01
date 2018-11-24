# 导包
from appium import webdriver
# 声明字典
desired_caps = {}
# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '5.1'
# 必填
# desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['deviceName'] = 'emulator-5554'
# APP包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'
# 获取driver
webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)