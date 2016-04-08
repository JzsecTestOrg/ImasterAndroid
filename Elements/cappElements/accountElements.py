# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback
import time


def openaccountButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('account', 'account', 'openaccountButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件openaccountButton未找到\n" + traceback.format_exc())


def videoreadyButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('account', 'account', 'videoreadyButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件videoreadyButton未找到\n" + traceback.format_exc())


def endvideoButton(self):
    try:
        el = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, Data.getXpath('account', 'account', 'endvideoButton', 1))))
        time.sleep(5)
        return el
    except:
        globalData.LOG += generateLog.format_log("控件endvideoButton未找到\n" + traceback.format_exc())


def confirmendvideoButton(self):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('account', 'account', 'confirmendvideoButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件confirmendvideoButton未找到\n" + traceback.format_exc())


