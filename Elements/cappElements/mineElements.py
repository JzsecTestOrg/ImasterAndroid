# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback

def loginentranceButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'loginentranceButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件loginentranceButton未找到\n" + traceback.format_exc())


def logoutButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'logoutButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件logoutButton未找到\n" + traceback.format_exc())


def backButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('mine', 'mine', 'backButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件backButton未找到\n" + traceback.format_exc())
