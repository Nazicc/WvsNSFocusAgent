#/usr/bin/env python
#coding=utf-8

import time
# from selenium.webdriver.common.action_chains import ActionChains

from app.config import *
from app.xpath import *
from . import *

# 页面切换类
class ViewSwitch(object):

    def __init__(self, browser):
        self.browser = browser
    # 切换到任务列表页面
    def vulListViewShow(self):
        self.taskListViewShow()
        task = self.browser.find_element_by_xpath(taskListsTrXpath)
        taskInfo = TaskInfo(self.browser,task)
        taskInfo.getTaskInfo()
        taskInfo.taskDescLink.click()
        time.sleep(5)
        self.browser.find_element_by_xpath(xpathTaskInfoViewSel["xpathVulListViewSel"]).click()

    # 切换到任务列表页面
    def taskListViewShow(self):
        self.browser.switch_to.parent_frame()
        self.browser.find_element_by_xpath(taskListViewShowXpath).click()
        time.sleep(5)
        self.browser.switch_to_frame("mainFrame")   

    # 切换到新建任务页面
    def taskCreateViewShow(self):
        self.browser.switch_to.parent_frame()
        self.browser.find_element_by_xpath(taskCreateViewShowXpath).click()
        time.sleep(5)
        self.browser.switch_to_frame("mainFrame")        