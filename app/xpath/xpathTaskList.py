#!/usr/bin/env python
#coding:utf-8
# 任务列表菜单
taskListViewShowXpath = '//*[@id="two02"]'
taskListsTrXpath =  '//*[@id="task_info"]/tbody/tr'


# Task Progress page
taskProgressCtrlXpath={
    'pause':'//*[@id="pause"]',
    'stop':'//*[@id="control_button"]/input[2]',
    'return':'//*[@id="control_button"]/input[3]'
}

# 任务列表中每一项内容的xpath
taskListViewXpath = {
    'checkBox':'//*[@id="task_info"]/tbody/tr[1]/td[1]/input',
    'taskId':'//*[@id="task_info"]/tbody/tr[1]/td[2]',
    'taskDesc':'//*[@id="task_info"]/tbody/tr[1]/td[3]/a',#点击后进入任务详细信息
    'taskType':'//*[@id="task_info"]/tbody/tr[1]/td[4]/img',
    'runType':'//*[@id="task_info"]/tbody/tr[1]/td[5]/img',
    'startTime':'//*[@id="task_info"]/tbody/tr[1]/td[6]',
    'stopTime':'//*[@id="task_info"]/tbody/tr[1]/td[7]',
    'cmnProgress':'//*[@id="task_info"]/tbody/tr[1]/td[8]/span[2]',#任务完成百分比
    'taskStatus':'//*[@id="task_info"]/tbody/tr[1]/td[9]',# 任务终止、任务完成，暂停中（点击暂停按钮后）、暂停、继续扫描中（点击继续扫描后），正在运行
    'taskHandle':'//*[@id="task_info"]/tbody/tr[1]/td[10]'# title：任务删除、任务断点续扫、任务重新扫描、暂停、停止
}
# 操作确认对话框，位于index框架，需要先切换到index中：
taskHandleComfirm = {
    "yes":'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/input[1]',
    "cancel":'/html/body/div[3]/div[2]/div[2]/div[2]/div/div/input[2]'
}