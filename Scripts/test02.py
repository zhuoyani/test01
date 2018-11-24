# 导包
from time import sleep

from appium import webdriver
"""前置代码："""
# 声明字典
desired_caps = {}
# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '5.1'
# 必填
desired_caps['deviceName'] = '192.168.56.101:5555'
# APP包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'
# 获取driver
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

"""
需求：
    1. 打开设置页面
    2. 暂停3秒
    3. 打开短信页面   
    4. 关闭app 
"""
# 暂停3秒
sleep(3) # 单位秒
# 调用Appium启动应用方法 打开短信页面  com.android.mms/.ui.ConversationList
driver.start_activity("com.android.mms",".ui.ConversationList")
# 关闭 APP
# driver.close_app()
# 关闭驱动对象 [推荐]
driver.quit()