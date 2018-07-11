#/usr/bin/env python
#coding=utf-8

import time
# from selenium.webdriver.common.action_chains import ActionChains

from app.config import *
from app.xpath import *
from . import *

# 切换到任务列表页面
def taskListViewShow(browser):
    browser.switch_to.parent_frame()
    browser.find_element_by_xpath(taskListViewShowXpath).click()
    time.sleep(3)
    browser.switch_to_frame("mainFrame")

# taskinfo 类测试
def clPrintTaskList(browser):
    taskListViewShow(browser)

    # taskList = '//*[@id="task_info"]/tbody/tr'
    taskLines = browser.find_elements_by_xpath(taskListsTrXpath)
    
    for task in taskLines:
        taskInfo = TaskInfo(browser,task)
        taskInfo.getTaskInfo()
        taskInfo.printTaskInfo()
        taskInfo.taskReScan()



class TaskInfo():
    # 
    # 
    def __init__(self,driver,trElement):
        self.taskId = "1"
        self.taskDesc = "扫描[]"
        self.taskType = "风险评估任务"
        self.runType = "立即任务"
        self.startTime = "2018-04-17  10:21:32"
        self.stopTime = "2018-04-17  10:26:11"
        self.cmnProgress = "0.00%"
        self.taskStatus = "任务终止"
        # self.taskHandles = taskHandle[2]
        self.taskDescUrl = ""
        self.browser = driver
        self.tr = trElement
        self.taskHandles = ["任务删除","任务停止","任务暂停","任务继续扫描","任务断点续扫","周期任务删除","重扫任务删除","任务重新扫描","周期任务暂停","周期任务续扫"]
        self.taskStatuses = ["任务终止","任务完成","暂停中","暂停","继续扫描中","正在运行"]        

    #
    # 
    #  获取任务信息
    def getTaskInfo(self):
        task = self.tr
        # print(task.text)
        el = task.find_element_by_xpath('td[2]')        
        self.taskId = el.text

        el = task.find_element_by_xpath('td[3]')        
        self.taskDesc = el.text        
        self.taskDescUrl = self.getTaskDescUrl(el)

        el = task.find_element_by_xpath('td[6]')
        # print(u"任务开始时间:" + el.text)
        self.startTime = el.text        

        el = task.find_element_by_xpath('td[7]')
        # print(u"任务结束时间:" + el.text)
        self.stopTime = el.text        

        el = task.find_element_by_xpath('td[9]')
        # print(u"任务状态:" + el.text)
        self.taskStatus = el.text      

        el = task.find_element_by_xpath('td[8]')
        # print(u"任务进度:" + el.text)
        self.cmnProgress = el.text      

        self.tdHandles = task.find_element_by_xpath('td[10]')
    
    # 获取任务详细信息链接
    def getTaskDescUrl(self, tdElement):
        el = tdElement.find_element_by_xpath('a')
        # 任务详细链接页面对象，可以通过click函数直接查看
        self.taskDescLink = el
        return el.get_attribute("href")

    # 打印任务信息
    def printTaskInfo(self):
        print(self.taskId)
        print(self.taskDesc)
        print(self.taskType)
        print(self.runType)
        print(self.startTime)
        print(self.stopTime)
        print(self.cmnProgress)
        print(self.taskStatus)
        # self.taskHandles = taskHandle[2]
        print(self.taskDescUrl)

    # 获取任务状态
    def getTaskStatus(self):
        task = self.tr

        el = task.find_element_by_xpath('td[9]')
        # print(u"任务状态:" + el.text)
        self.taskStatus = el.text      
        return self.taskStatus
   
    # 获取任务运行进度
    def getCmnProgress(self):
        task = self.tr
        el = task.find_element_by_xpath('td[8]')
        # print(u"任务进度:" + el.text)
        self.cmnProgress = el.text      
        return self.cmnProgress


    # 任务操作
    # taskHandles = ["任务删除","任务停止","任务暂停","任务继续扫描","任务断点续扫","周期任务删除","重扫任务删除","任务重新扫描","周期任务暂停","周期任务续扫"]    
    # 删除任务
    def taskDel(self):
        self.taskHandle(u"任务删除")
    
    # 停止任务
    def taskStop(self):
        self.taskHandle(u"任务停止")

    # 暂停任务
    def taskPause(self):
        self.taskHandle(u"任务暂停")

    # 继续扫描任务，任务状态是：暂停
    def taskContinue(self):
        self.taskHandle(u"任务继续扫描")

    # 重新扫描任务，任务状态是：任务完成
    def taskReScan(self):
        self.taskHandle(u"任务重新扫描")

    # 断点续扫，任务状态是：停止
    def taskStartFromLastPos(self):
        self.taskHandle(u"任务断点续扫")

    def taskHandle(self, handleType):
        els= self.tdHandles.find_elements_by_xpath('div/img')
        if handleType==u"任务删除":
            for el in els:                
                if el.get_attribute('title')==handleType:
                    self.taskHandlePerform(el)
                    break
            print(u"当前任务状态中不存在操作类型："+ handleType)                                                                                                    
        elif handleType==u"任务停止":
            for el in els:                
                if el.get_attribute('title')==handleType:
                    self.taskHandlePerform(el)
                    break
            print(u"当前任务状态中不存在操作类型："+ handleType)                                                                                                    
        elif handleType==u"任务暂停":
            for el in els:                
                if el.get_attribute('title')==handleType:
                    self.taskHandlePerform(el)
                    break
            print(u"当前任务状态中不存在操作类型："+ handleType)                                                                                                    
        elif handleType==u"任务继续扫描":
            for el in els:                
                if el.get_attribute('title')==handleType:
                    self.taskHandlePerform(el)
                    break
            print(u"当前任务状态中不存在操作类型："+ handleType)                                                                                
        elif handleType==u"任务重新扫描":
            for el in els:                
                if el.get_attribute('title')==handleType:
                    self.taskHandlePerform(el)
                    break
            print(u"当前任务状态中不存在操作类型："+ handleType)                                                                                
        elif handleType==u"任务断点续扫":
            for el in els:                
                if el.get_attribute('title')==handleType:
                    self.taskHandlePerform(el)
                    break  
            print(u"当前任务状态中不存在操作类型："+ handleType)                                                                                
        else:
            print(u"当前任务状态中不存在操作类型："+ handleType)

    # 任务操作执行
    def taskHandlePerform(self, el):
        print(el.get_attribute('title'))
        # 操作
        el.click()
        time.sleep(3)
        # 确认操作
        self.browser.switch_to.parent_frame()
        self.browser.find_element_by_xpath(taskHandleComfirm["cancel"]).click() #取消
        # self.browser.find_element_by_xpath(taskHandleComfirm["yes"]).click() #确认
        # time.sleep(10) # 确认执行时等待事件长一些        
        time.sleep(3)
        self.browser.switch_to_frame("mainFrame")