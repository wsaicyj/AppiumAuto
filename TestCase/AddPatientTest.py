#! /usr/bin/env pthon3
# -*- coding:utf-8 -*-
__author__ = 'Aaron_chan'

from PageObject.Newhealth.PatientManagePage import PatientManagePage
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
# from PageObject.Home.FirstOpenPage import FirstOpenPage
from PageObject.Newhealth.LoginPage import LoginPage
from TestCase.Login import Login

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AddPatientTest(ParametrizedTestCase):
    '''就诊人管理界面'''

    def test_add_patient(self):
        '''测试添加就诊人功能'''
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Newhealth/test_patient.yaml"),
               "device": self.devicesName, "caseName": sys._getframe().f_code.co_name}

        page = PatientManagePage(app)
        page.operate()
        page.checkPoint()




    @classmethod
    def setUpClass(cls):
        super(AddPatientTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(AddPatientTest, cls).tearDownClass()
