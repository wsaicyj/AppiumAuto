#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-


__author__ = 'Aaron_chan'



from Base.BaseRunner import ParametrizedTestCase
import os
import sys
# from PageObject.Home.FirstOpenPage import FirstOpenPage
from PageObject.Newhealth.LoginPage import LoginPage


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginTest(ParametrizedTestCase):

    # def test_my_click(self):
    #     '''测试点击我的模块'''
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Newhealth/test_my_click.yaml"),
    #            "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}
    #
    #     page = LoginPage(app)
    #     page.operate()
    #     page.checkPoint()


    def test_login(self):
        '''测试登录功能'''
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Newhealth/test_login.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        page.checkPoint()



    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
