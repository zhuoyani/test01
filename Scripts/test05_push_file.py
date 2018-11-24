# 导包
import base64

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
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

"""
    需求：
        1. 把当前目录下test222.txt发送到手机sdcard目录下名为test333.txt
"""
with open("./test222.txt","r",encoding="utf-8") as f:
    # data=str(base64.b64encode(f.read().encode("utf-8")),"utf-8")

    # base64.base64.b64encode(f.read()) 返回的类型 bytes
    data=str(base64.b64encode(f.read().encode("utf-8")),"utf-8")
    # 调用 appium 发送文件的方法
    driver.push_file("/sdcard/test333.txt",data)

    """
        b64encode:为加密成base64位
    """