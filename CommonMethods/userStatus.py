# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

import dataBase, globalData, generateLog, Data

#注册状态
def isRegisterSuccess(phone):
    count = len(dataBase.imaster_info(phone))
    if(count == 0):
        globalData.LOG += generateLog.format_log("手机号" + str(phone) + " 未注册")
        return False
    else:
        globalData.LOG += generateLog.format_log("手机号" + str(phone) + " 已注册")
        return True

if __name__ == '__main__':
    if(isRegisterSuccess(Data.getTestdata('register', 1, 2))):
        print 'ok'
            # dataBase.delete_cuser(Data.getTestdata('register', 1, 2))

