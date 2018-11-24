# 导包
from time import sleep

import os
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
        1. 判断AK_CRM是否已安装
        2. 已安装进行卸载
        3. 未安装进行安装
"""
# 判断是否安装AK_CRM  如果安装了，返回 True
# if driver.is_app_installed("com.vcooline.aike"):
try:
    if driver.is_app_installed("com.tencent.news"):
        # 卸载 AK_CRM应用
        driver.remove_app("com.tencent.news")
        print("卸载成功！")
    else:
        # 安装 AK_CRM应用
        # driver.install_app("C:\\tengxun.apk")
        driver.install_app(os.getcwd()+os.sep+"tengxun.apk")
        print("安装成功！")
except:
    pass