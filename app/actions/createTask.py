#/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from app.config import *
from app.xpath import *
from . import *


class TaskCreate(object):
    def __init__(self, browser):
        self.browser = browser

    def taskCreateAndRun(self):
        self.taskCreate(self.browser)
        time.sleep(3)
        
        self.taskRun(self.browser)
        time.sleep(10)
    
    def taskCreate(self,taskConfig):
        self.taskConfig = taskConfig
        self.commonConfigFill()
        # 高级配置

        
        self.advanceConfigFill()


    def commonConfigFill(self):
        # 扫描对象
        el = self.browser.find_element_by_xpath(taskConfigXpath["scanTarget"])
        el.click()    
        el.send_keys(self.taskConfig["scanTarget"])
        time.sleep(1)

        # 任务名称
        el = self.browser.find_element_by_xpath(taskConfigXpath["taskName"])
        el.click()
        time.sleep(1)

        # 扫描范围
        el = self.browser.find_element_by_xpath(taskConfigXpath["scanRange"])
        sel = Select(el)
        sel.select_by_value(self.taskConfig['scanRange'])
        time.sleep(1)
        # 运行方式
        el = self.browser.find_element_by_xpath(taskConfigXpath["runType"])
        sel = Select(el)
        sel.select_by_value(self.taskConfig['runType'])
        time.sleep(1)

        # 插件模板
        el = self.browser.find_element_by_xpath(taskConfigXpath["pluginTemplate"])
        sel = Select(el)
        sel.select_by_value(self.taskConfig['pluginTemplate'])
        time.sleep(1)     



    def advanceConfigFill(self):
        self.browser.find_element_by_xpath(taskConfigAdvanceXpath["showXpath"]).click()
        time.sleep(1)

    def taskRun(self):
        el = self.browser.find_element_by_xpath(taskConfigSubmitAndRunXpath).click()        

     
    