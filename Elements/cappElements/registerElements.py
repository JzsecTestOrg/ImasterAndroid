# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from CommonMethods import Data, globalData, generateLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import traceback

def registerPage(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'registerPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件registerPage未找到\n" + traceback.format_exc())


def phoneText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'phoneText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件phoneText未找到\n" + traceback.format_exc())


def vercodeButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'vercodeButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeButton未找到\n" + traceback.format_exc())


def vercodeText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'vercodeText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件vercodeText未找到\n" + traceback.format_exc())

def passwordText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'passwordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件passwordText未找到\n" + traceback.format_exc())


def plainpasswordText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'plainpasswordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件plainpasswordText未找到\n" + traceback.format_exc())

def cipherpasswordText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'cipherpasswordText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件cipherpasswordText未找到\n" + traceback.format_exc())


def eyeopenButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'eyeopenButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyeopenButton未找到\n" + traceback.format_exc())


def eyecloseButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'eyecloseButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件eyecloseButton未找到\n" + traceback.format_exc())


def nicknameText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'nicknameText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件nicknameText未找到\n" + traceback.format_exc())


def protocolCheckbox(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolCheckbox', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolCheckbox未找到\n" + traceback.format_exc())


def protocolLink(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolLink未找到\n" + traceback.format_exc())


def protocolPage(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolPage未找到\n" + traceback.format_exc())


def protocolText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'protocolText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件protocolText未找到\n" + traceback.format_exc())


def registerButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'registerButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件registerButton未找到\n" + traceback.format_exc())


def servicephoneText(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'servicephoneText', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件servicephoneText未找到\n" + traceback.format_exc())


def registefinishPage(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'registefinishPage', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件registefinishPage未找到\n" + traceback.format_exc())


def seefirstLink(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'seefirstLink', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件seefirstLink未找到\n" + traceback.format_exc())

def backButton(self):
    try:
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, Data.getXpath('register', 'register', 'backButton', 1))))
        return el
    except:
        globalData.LOG += generateLog.format_log("控件backButton未找到\n" + traceback.format_exc())





