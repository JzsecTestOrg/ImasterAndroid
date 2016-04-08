# -*- coding: UTF-8 -*-
__author__ = 'xuwen'

from Elements.cappElements import welcomeElements
from CommonMethods import globalData, generateLog





def welcome(self):
    try:
        welcomeElements.experienceButton(self).click()
        globalData.LOG += generateLog.format_log("点击‘立即体验’")
    except:
        globalData.LOG += generateLog.format_log("未显示欢迎页面")








