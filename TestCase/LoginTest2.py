#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
from PageObject.Newhealth.LoginPage2 import LoginPage2

__author__ = 'Aaron_chan'



from Base.BaseRunner import ParametrizedTestCase
import os
from TestCase.Login import Login
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginTest2(ParametrizedTestCase):


    def test_login(self):
        '''测试登录功能'''
        # Login.login(self)
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Newhealth/test_login.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = LoginPage2(app)
        page.operate()
        page.checkPoint()


    @classmethod
    def setUpClass(cls):
        super(LoginTest2, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest2, cls).tearDownClass()
