import os
# getcwd() 获取当前文件的绝对路径
# sep：动态获取目录分隔符 window获取\ mac获取出来的/
print(os.getcwd())
print(os.getcwd()+os.sep+"AK_CRM.apk")