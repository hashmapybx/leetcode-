# _*_ coding: utf-8 _*_
# @Time : 2021/7/23/0023 17:13 
# @Author : 流柯 
# @Version：V 0.1
# @File : wifi.py
# @desc :

import pywifi
from pywifi import const    #获取连接状态的常量库
import time
# 抓取网卡接口
wifi = pywifi.PyWiFi()
# 获取第一个无线网卡
ifaces = wifi.interfaces()[0]
# 断开网卡连接
ifaces.disconnect()
time.sleep(1)
# 获取wifi的连接状态
wifistatus = ifaces.status()
# 网卡断开链接后开始连接测试
if wifistatus == const.IFACE_DISCONNECTED:
    # 创建wifi连接文件
    profile = pywifi.Profile()
    # 要连接的wifi的名称  貌似不能用中文？
    profile.ssid = '9168hfh'
    # 网卡的开放状态 | auth - AP的认证算法
    profile.auth = const.AUTH_ALG_OPEN
    # wifi的加密算法，一般wifi 加密算法时wps  #选择wifi加密方式  akm - AP的密钥管理类型
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    # 加密单元 /cipher - AP的密码类型
    profile.cipher = const.CIPHER_TYPE_CCMP
    # 调用密码 /wifi密钥 如果无密码，则应该设置此项CIPHER_TYPE_NONE

else:
    print("已有wifi连接")