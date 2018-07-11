#/usr/bin/env python
#coding=utf-8

import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from app.config import *
from app.xpath import *
from . import *


# 切换到任务列表页面
def reportExportViewShow(browser):
    browser.switch_to.parent_frame()
    browser.find_element_by_xpath(reportExportXpath).click()
    time.sleep(3)
    browser.switch_to_frame("mainFrame")

def reportTest(browser,taskId,taskName):
    reportExportViewShow(browser)

    taskReport = Report(browser,taskId,taskName)
    taskReport.createReport()
    taskReport.exportReport()
    taskReport.unzipReport()

class Report(object):
    def __init__(self,browser,taskId,taskName):
        self.taskId = taskId
        self.browser = browser
        self.taskName = taskName

    def createReport(self):
        # 选择任务
        taskSel = self.browser.find_element_by_xpath(xpathReportExportConfig["task"])
        # taskSelText = self.taskId+"--" + self.taskName
        taskSel.click()
        time.sleep(2)
        tasks = self.browser.find_elements_by_xpath('//*[@id="task_id"]/div/ul/li')
        for task in tasks:
            label = task.find_element_by_xpath('label')
            if label.get_attribute('for')==self.taskId:
                label.click()
                ActionChains(self.browser).move_to_element(taskSel)
                break
        
        self.browser.find_element_by_xpath(xpathReportExportConfig['reportName']).click()
        time.sleep(5)
        self.browser.find_element_by_xpath(xpathReportExportConfig['reportTypeXls']).click()
        time.sleep(1)
        self.browser.find_element_by_xpath(xpathReportExportConfig['reportCreate']).click()
        time.sleep(15)


    def exportReport(self):
        # el = self.browser.find_element_by_xpath('//div[@class="J-paginator-1"]')
        el = self.browser.find_element_by_xpath('//div[@class="J-paginator-1"]/div[2]/table/tbody/tr/td[1]/a')
        print(el.text)
        print(el.get_attribute("href"))
        el.click()
        time.sleep(10)        

    def unzipReport(self):
        
        os.system("unzip result/*.zip")
        time.sleep(10)
        os.system("rm result/*.zip")
