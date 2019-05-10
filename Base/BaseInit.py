#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from Base.BaseElementEnmu import Element
from Base.BasePickle import *
from Base.BaseFile import *
from Base.BaseApk import *
from Base.BaseIpa import *
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

apkPath = PATH("../app/NewHealthApp_201902261509_test_v2.9.0.apk")  # 安卓测试的app路径
ipaPath = PATH("../app/NewHealthApp_201901041724_test_v2.8.0.ipa")  # IOS测试的app路径

def mk_file(platform):
    destroy()
    mkdir_file(PATH("../Log/" + Element.INFO_FILE))
    mkdir_file(PATH("../Log/" + Element.SUM_FILE))
    mkdir_file(PATH("../Log/" + Element.DEVICES_FILE))

    data = read(PATH("../Log/" + Element.INFO_FILE))
    if platform == 'android':
        apkInfo = ApkInfo(apkPath).getApkBaseInfo()
        data["appName"] = ApkInfo(apkPath).getApkName()
        data["packageName"] = apkInfo[0]
        data["appVersion"] = apkInfo[2]

        data["sum"] = 0
        data["pass"] = 0
        data["fail"] = 0
        write(data=data, path=PATH("../Log/" + Element.SUM_FILE))
    elif platform == 'iOS':
        ipaInfo = getIpaInfo(ipaPath)
        data["appName"] = ipaInfo[0]
        data["packageName"] = ipaInfo[1]
        data["appVersion"] = ipaInfo[2]

        data["sum"] = 0
        data["pass"] = 0
        data["fail"] = 0
        write(data=data, path=PATH("../Log/" + Element.SUM_FILE))


def init(devices):
    # 每次都重新安装uiautomator2都两个应用
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server.test" % devices)
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server" % devices)
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-v2.8.0.apk")))
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-debug-androidTest.apk")))
    # os.popen("adb install -r "+PATH("../app/android-system-webview-60.apk"))


def destroy():
    remove_file(PATH("../Log/"+Element.INFO_FILE))
    remove_file(PATH("../Log/"+Element.SUM_FILE))
    remove_file(PATH("../Log/"+Element.DEVICES_FILE))


if __name__ == '__main__':
    # print(destroy())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    rq = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
    print(rq)
