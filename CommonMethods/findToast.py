# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback
import time

def find_toast(self, message):
    try:
        el = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
        globalData.LOG += generateLog.format_log("提示" + message + "显示正确")
        return True
    except:
        globalData.LOG += generateLog.format_log("控件未找到\n" + traceback.format_exc())
        return False
