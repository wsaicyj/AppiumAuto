#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-

__author__ = 'Aaron_chan'

# from theano import pp
from Base import BaseInit

import sys
import platform
from Base.BaseAndroidPhone import *
from Base.BaseAdb import *
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import init, mk_file
from Base.BaseStatistics import countDate, writeExcel, countSumDevices
from Base.BasePickle import *
from datetime import datetime
from Base.BaseApk import ApkInfo
from TestCase.AddPatientTest import AddPatientTest
from TestCase.HomeTest import HomeTest
from TestCase.LoginTest import LoginTest

sys.path.append("..")
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def kill_adb():
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")

def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]

        _initApp["app"] = getDevices[i]["app"]
        apkInfo = ApkInfo(_initApp["app"])
        _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        _initApp["appActivity"] = apkInfo.getApkActivity()
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(AddPatientTest, param=devices)) #就诊人管理
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices)) #加入测试类
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")

if __name__ == '__main__':

    kill_adb()

    devicess = AndroidDebugBridge().attached_devices()
    if len(devicess) > 0:
        mk_file('android')
        l_devices = []
        for dev in devicess:
            app = {}
            app["devices"] = dev
            # init(dev)
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))
            app["app"] = BaseInit.apkPath
            # app["app"] = PATH("../app/NewHealthApp_201901041724_test_v2.8.0.apk")

            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()   #启动appium服务
        runnerPool(l_devices)
        writeExcel()
        appium_server.stop_server(l_devices)
    else:
        print("没有可用的安卓设备")
