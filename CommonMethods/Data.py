# -*- coding: utf-8 -*-
__author__ = 'xuwen'

import xlrd
from pyexcel_xls import XLBook
import sys
import os
import globalData



def getXpath(tab, page, element, index):
    worksheet = globalData.XPATH.get(tab)
    nrows = len(worksheet)
    for i in range(1, nrows):
        if(worksheet[i][0] == unicode(page,'utf-8')):
            if(worksheet[i][1] == unicode(element,'utf-8')):
                if(int(worksheet[i][2]) == int(index)):
                    return worksheet[i][3]
                    break


def getValue(tab, page, element, index):
    module = globalData.MODULE
    worksheet = globalData.XPATH.get(tab)
    nrows = len(worksheet)
    for i in range(0, nrows):
        if(worksheet[i][0] == unicode(page,'utf-8')):
            if(worksheet[i][1] == unicode(element,'utf-8')):
                if(int(worksheet[i][2]) == index):
                    return worksheet[i][4]
                    break


def getNumber(tab, page, element, index):
    module = globalData.MODULE
    worksheet = globalData.XPATH.get(tab)
    nrows = len(worksheet)
    for i in range(0, nrows):
        if(worksheet[i][0] == unicode(page,'utf-8')):
            if(worksheet[i][1] == unicode(element,'utf-8')):
                if(int(worksheet[i][2]) == index):
                    return str(worksheet[i][4]).split('.')[0]
                    break


def getMessage(tab, page, element, index):
    module = globalData.MODULE
    worksheet = globalData.XPATH.get(tab)
    nrows = len(worksheet)
    for i in range(0, nrows):
        if(worksheet[i][0] == unicode(page,'utf-8')):
            if(worksheet[i][1] == unicode(element,'utf-8')):
                if(int(worksheet[i][2]) == index):
                    return str(worksheet[i][6]).split('.')[0]
                    break


def getPrecondition(tab, case):
    worksheet = globalData.TESTDATA.get(tab)
    return worksheet[case][1]


def getTestdata(tab, case, index):
    worksheet = globalData.TESTDATA.get(tab)
    if('.' in str(worksheet[case][index])):
        return  str(worksheet[case][index]).split('.')[0]
    else:
        return worksheet[case][index]

def getCasenumber(moudle):
    worksheet = globalData.TESTDATA.get(moudle)
    nrows = len(worksheet)
    return nrows







if __name__ == '__main__':
    # print Data()
    # print sys.path
    # print os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # print getXpath('welcome', 'versionUpdate_cancel', 1)
    print getXpath('login', 'login', 'backButton', '1')
    # print getXpath('welcome', 'versionUpdate_cancel', 1)
    # globalData.MODULE = 'register'
    # print unicode("输入昵称: ", 'utf-8') + getValue('register', 'nicknameText', 1)
    # print getTestdata('register', 2, 13)


