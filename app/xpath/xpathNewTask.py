#!/usr/bin/env python
#coding:utf-8
from config import baseInfo

# 新建任务菜单
taskCreateViewShowXpath = '//*[@id="two01"]'
taskViewUrl = baseInfo["wvssServerUrl"]+"/task"

taskConfigXpath={
    "scanTarget":"//*[@id=\"task_target\"]",
    "taskName":"//*[@id=\"task_name\"]",
    "scanRange":"/html/body/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[7]/td[2]/select",
    # "scanRange":"*[@name=\"scan_method\"]",
    "runType":"//*[@id=\"operate\"]",
    "pluginTemplate":"//*[@id=\"plugin_templates\"]"
}

taskConfigAdvanceXpath={
    "showXpath":"/html/body/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[13]/td[2]/div/span",
    "taskDescription":"//*[@id=\"task_description\"]",
    "reportAutoExport":"//*[@id=\"J-report-way\"]/div[6]/label/input",
    "pluginsThreads":"//*[@id=\"plugin_threads\"]",
    "scanTimeOut":"//*[@id=\"webaccess\"]/table/tbody/tr[4]/td[2]/input",
    "authName":"//*[@id=\"proxy_auth\"]/table/tbody/tr[2]/td[2]/input",
    "authPassword":"//*[@id=\"J-authpwd\"]"
}
taskConfigSubmitAndRunXpath = "//*[@id=\"create_task\"]"