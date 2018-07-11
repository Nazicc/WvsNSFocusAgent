
#/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

from app.config   import *
from app.actions import *


controller = TaskController()
controller.taskCreateAndRun()
controller.taskRunMonitor()
# firefox = FirefoxBrowser()
# browser = firefox.getBrowser()

# login(browser)

# # taskCreateAndRun(browser)
# # printTaskList(browser)
# # clPrintTaskList(browser)
# # reportTest(browser,'204',u'扫描[https://192.168.1.2]')
# # vulListViewShow(browser)

# switch = ViewSwitch(browser)
# switch.taskCreateViewShow()

# taskCreater = TaskCreate(browser)
# taskCreater.taskCreate(taskConfig)
# taskCreater.taskRun()
# time.sleep(10)
# switch.taskListViewShow()
time.sleep(20)
# switch.vulListViewShow()

# vulParse = VulListParse(browser,204)
# vulParse.parseVulList()
# vulParse.scanReuslt.printResult()

    # vulParse = VulListParse(browser,204)
    # vulParse.parseVulList()
    # for vulInfo in vulParse.scanReuslt.vulInfo:
    #     vulInfo.printVulInfo()
# controller.taskStopMonitor()
# controller.browserQuit()
# browser.close()