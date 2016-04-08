# -*- coding: utf-8 -*-
__author__ = 'xuwen'

import os
import Data
from pyexcel_xls import XLBook


#Bapp测试环境
BASE_URL_PATH_BROKER = "http://t.a.jzsec.com/"

#Bweb测试环境
BASE_URL_PATH_BWEB = "http://t.b.jzsec.com/"

#Bweb登录接口
BWEB_LOGIN = "site/login"

#身份证审核接口
AFFILIATE_AUDITID = "buser/auditid"

#合同签收接口
SIGN_CONTRACT = "buser/signcontract"

#SAC账号接口
SAC_ACCOUNT = "buser/auditcer"

#执业证书编号接口
SAC_ID = "buser/auditcerid"

#SAC审核/年审
SAC_APPROVE = "buser/auditcerstatus"

#项目路径
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

#Xpath
file_path = PATH + '/TestData/Capp.xlsx'
workbook = XLBook(file_path)
test_data = dict(workbook.sheets())
XPATH = test_data

#测试数据集
file_path1 = PATH + '/TestData/CappTestData.xlsx'
workbook1 = XLBook(file_path1)
test_data1 = dict(workbook1.sheets())
TESTDATA = test_data1

#模块名称
MODULE = ''
# MODULE = sys.argv[0][sys.argv[0].rfind(os.sep)+1:].split('.')[0]
# MODULE = inspect.stack()[1][3]

#日志信息
LOG = ''

#视频接入开始时间
START = []

#视频接入结束时间
END = []

#实际视频接入时间
TOTAL = []

#执行结果
RESULT = []

#真机启动结果
INIT = []

#用例执行结果
RESULT = []

#执行过的模块
EXECUTED = []










