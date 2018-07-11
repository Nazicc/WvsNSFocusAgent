#/usr/bin/env python
# -*- coding: UTF-8 -*-


taskRunType = ["directory","timming","everyday","everyweek","everymonth","everymonth_week"]
scanRange = ['0','1','2']   # 0：按域名扫描，1：扫描当前目录及子目录，2：只扫描任务目标链接
pluginTemplate = ['100','102','103'] #100:Web应用漏洞(全部);  102:快速扫描; 103:高危漏洞扫描
taskConfig={
    "scanTarget":"https://192.168.1.2",
    "taskName":"Scan[https://192.168.1.2]",
    'scanRange':scanRange[1],
    'runType':taskRunType[0],
    "pluginTemplate":pluginTemplate[0]
}
taskConfigXpath={
    "scanTarget":"//*[@id=\"task_target\"]",
    "taskName":"//*[@id=\"task_name\"]",
    # "scanRange":"/html/body/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/table/tbody[1]/tr[7]/td[2]/select",
    "scanRange":"*[@name=\"scan_method\"]",
    "runType":"//*[@id=\"operate\"]",
    "pluginTemplate":"//*[@id=\"plugin_templates\"]"
}
taskConfigAdvance={
# //*[@id="task_target"]
}