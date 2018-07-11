#/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import threading
import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

from app.config   import *
from app.actions import *

#########################################################################################################
# 配置并创建火狐浏览器
class FirefoxBrowser(object):
    
    # 下载文件类型
    FILETYPE_MIME = {
                "txt":"text/plain",
                "pdf":"application/pdf",
                "csv":" text/csv",
                "zip":"application/zip",
                "bin": "application/octet-stream",
                "doc": "application/msword",
                "ppt": "application/vnd.ms-powerpoint",
                "xls": "application/vnd.ms-excel",
                "docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document ",
                "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",                
                "xlsx":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "ppsx":"application/vnd.openxmlformats-officedocument.presentationml.slideshow"
                }      
                
    savePath = "/home/lyz/Workspace/pyWork/nsfocus/result"
    def __init__(self):
        self.opt = Options()
        self.profile = webdriver.FirefoxProfile()
        self.desired_capabilities = None
        # self.set_opt()
        # self.set_proxies()
        self.setProfile()
        # self.savePath = "result"

    def getBrowser(self):
        self.driver = webdriver.Firefox(    
                                        executable_path="geckodriver",
                                        capabilities=self.desired_capabilities,
                                        firefox_options = self.opt,
                                        firefox_profile=self.profile
                                        )
        return self.driver

    def setProfile(self):
        # 设置下载文件保存路径        
        self.profile.set_preference("browser.download.folderList",2)
        self.profile.set_preference("browser.download.dir", self.savePath)
        # self.profile.set_preference("browser.download.useDownloadDir",True)
        # 不会打开未知MIMe类型 
        self.profile.set_preference("browser.helperApps.alwaysAsk.force",False)
        self.profile.set_preference("browser.download.manager.showWhenStarting",False)
        self.profile.set_preference("pdfjs.disabled",False)

        content_type=""
        for mime in self.FILETYPE_MIME:
            content_type = content_type+ self.FILETYPE_MIME[mime] +','
        
        content_type =content_type + "*/*"
        # print(content_type)

        self.profile.set_preference("browser.helperApps.neverAsk.saveToDisk",content_type)
        self.profile.set_preference("browser.helperApps.neverAsk.openFile",content_type)
        # 不会弹出警告框
        self.profile.set_preference("browser.download.manager.alertOnEXEopen",False)
        self.profile.set_preference("browser.download.manager.focusWhenStarting",False)
        self.profile.set_preference("browser.download.manager.useWindow",False)
        self.profile.set_preference("browser.download.manager.showAlertOnComplete",False)
        self.profile.set_preference("browser.download.manager.closewhenDone",False)

        self.profile.update_preferences()        




    def setOpt(self):
        self.opt.add_argument("-headless")

    def quit(self):
        self.driver.quit()
############################################################################################

class TaskController(object):
    


    def __init__(self):
        self.__isRunning = False
        self.__isEnd = False

        firefox = FirefoxBrowser()
        self.browser = firefox.getBrowser()

        login(self.browser)        

        self.switch = ViewSwitch(self.browser)


    def taskCreateAndRun(self, config = taskConfig):
        self.taskConfig = config
        self.switch.taskCreateViewShow()
        taskCreater = TaskCreate(self.browser)
        taskCreater.taskCreate(self.taskConfig)
        taskCreater.taskRun()
        time.sleep(20)


    def taskRunMonitor(self):
        self.switch.taskListViewShow()
        time.sleep(5)

        task = self.browser.find_element_by_xpath(taskListsTrXpath)
        self.taskInfo = TaskInfo(self.browser,task)
        self.getStatus()

        # self.timer = threading.Timer(2,self.getStatus)
        # self.timer.start()

    def getStatus(self):
        # print(u"任务状态:{1}    任务进度:{0}".format(self.taskInfo.getCmnProgress(),self.taskInfo.getTaskStatus()),end = '\r')
        taskStatus = self.taskInfo.getTaskStatus()
        cmnProgress = self.taskInfo.getCmnProgress()
        sys.stdout.write(u"任务状态:{1}    任务进度:{0}\r".format(cmnProgress,taskStatus))
        sys.stdout.flush()

        if "100%" == cmnProgress:
            self.__isEnd = True
            print(u"扫描完成")
            time.sleep(10)
            self.resultHandle()            
        else:
            self.timer = threading.Timer(2,self.getStatus)
            self.timer.start()
            
    def resultHandle(self):
        self.switch.vulListViewShow()
        self.vulParse = VulListParse(self.browser)
        self.vulParse.parseVulList()
        self.vulParse.scanReuslt.printResult()
        
        time.sleep(10)
        self.browserQuit()

    def taskStopMonitor(self):
        self.timer.cancel()
        self.__isEnd = False
        self.__isRunning = False

    def browserQuit(self):
        self.browser.quit()


