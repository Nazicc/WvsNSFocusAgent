#/usr/bin/env python
#coding=utf-8

import time
from queue import Queue

from app.config import *
from app.xpath import *
from . import *


class ScanResult(object):
    def __init__(self, taskId):
        self.taskId = taskId
        self.vulInfo = list()
    def printResult(self):
        for vulInfo in self.vulInfo:
            vulInfo.printVulInfo()

class VulInfo(object):
    def __init__(self):
        self.vulName = ""
        self.vulTimes = 0
        self.vulSite = ""
        self.urlList = list()
        # self.urlList = Queue.Queue()
        self.vulDetailDesc = ""
        self.vulResoleMethod = ""
        self.vulRisk = 0
        self.vulPlugins = ""
        self.vulDiscoverDate = ""
        self.vulCVE = ""        # 可以通过http://cve.mitre.org/cgi-bin/cvename.cgi?name={vulCVE}来查看漏洞信息
        self.vulBugTraq = ""    # 可以通过https://www.securityfocus.com/bid/{vulBugTraq}来查看详细信息
        self.vulCNNVD = ""
        self.vulCNCVE = ""
        self.vulCVSS = 0.0
        
    def printVulInfo(self):
        print(u"漏洞名称:\t"+self.vulName)
        print(u"出现次数:\t"+self.vulTimes)        
        print(u"受影响站点:\t"+self.vulSite)      
        # for i in range(self.urlList.qsize()):
        #     print(self.urlList.get())  
        print(u"受影响链接:\t")      
        for url in self.urlList:
               print("\t"+url)   
        print(u"详细描述:\t"+self.vulDetailDesc)        
        print(u"解决办法:\t"+self.vulResoleMethod)        
        print(u"威胁分值:\t%f" % self.vulRisk)        
        print(u"危险插件:\t"+self.vulPlugins)        
        print(u"发现日期:\t"+self.vulDiscoverDate)        
        print(u"CVE编号:\t"+self.vulCVE)        
        print(u"BUGTRAQ:\t"+self.vulBugTraq)        
        print(u"CNNVD编号:\t"+self.vulCNNVD)        
        print(u"CNCVE编号:\t"+self.vulCNCVE)                                                                            
        print(u"CVSS评分:\t%f" % self.vulCVSS)                

class VulListParse(object):

    def __init__(self, browser,taskId=1):
        self.browser = browser
        self.taskId = taskId
        self.scanReuslt = ScanResult(taskId)
        
    def parseVulList(self):
        vulTrElements = self.browser.find_elements_by_xpath(xpathVulInfoList["vulList"])
        totalNum = len(vulTrElements)        
        if totalNum<1:
            return 
        
        
        for index in range(1,totalNum/2+1):
            self.vulInfo = VulInfo()
            # 'vulName'       :   '//*[@id="vulDataTable"]/tbody/tr[{sIndex}]/td[1]', 
            vulNameXpath = xpathVulInfoList["vulName"].format(sIndex = 2*index-1)
            # print(vulNameXpath)
            el = self.browser.find_element_by_xpath(vulNameXpath)
            el.click()
            time.sleep(1)
            self.vulInfo.vulName = el.text
            # print(self.vulInfo.vulName)

            # 'vulTimes'      :   '//*[@id="vulDataTable"]/tbody/tr[{sIndex}]/td[2]',
            vulTimesXpath = xpathVulInfoList["vulTimes"].format(sIndex = 2*index-1)
            self.vulInfo.vulTimes = self.browser.find_element_by_xpath(vulTimesXpath).text
            # print(self.vulInfo.vulTimes)

            # 'vulDetailRow'  :   '//*[@id="vulDataTable"]/tbody/tr[{mIndex}]/td/table/tbody/tr' #mIndex是偶数，mIndex = sIndex +1
            vulDetailRowXpath = xpathVulInfoList["vulDetailRow"].format(mIndex = 2*index)
            # 获取漏洞详细信息TR列表，
            vulDetailElements = self.browser.find_elements_by_xpath(vulDetailRowXpath)
            self.getVulInfoDetails(vulDetailElements)

            self.scanReuslt.vulInfo.append(self.vulInfo)
            # self.vulInfo.printVulInfo()

    def getVulInfoDetails(self, elements):
        # totalNum = len(vulDetailElements) 
        for el in elements:
            th = el.find_element_by_xpath(xpathVulDetail['detailItemName'])
            detailItemName = th.text
            # print(detailItemName)

            td = el.find_element_by_xpath(xpathVulDetail['detailContent'])
            self.getDetailContent(detailItemName,td)

    def getDetailContent(self, detailItemName,tdElement):
        
        # 处理受影响站点行
        if u"受影响站点"==detailItemName:
            el = tdElement.find_element_by_xpath(xpathVulSiteInfo['vulSite'])
            self.vulInfo.vulSite = el.text
            
            el = tdElement.find_element_by_xpath(xpathVulSiteInfo['showUrls']).click()
            urlsText = tdElement.find_element_by_xpath(xpathVulSiteInfo['vulUrlList']).text                  
            urls = urlsText.split()
            for url in urls:
                # self.vulInfo.urlList.put(url) #队列
                self.vulInfo.urlList.append(url)
            
        elif u"详细描述"==detailItemName:            
            self.vulInfo.vulDetailDesc = tdElement.text

        elif u"解决办法"==detailItemName:            
            self.vulInfo.vulResoleMethod = tdElement.text

        elif u"威胁分值"==detailItemName:            
            self.vulInfo.vulRisk =float(tdElement.text)

        elif u"危险插件"==detailItemName:            
            self.vulInfo.vulPlugins = tdElement.text

        elif u"发现日期"==detailItemName:            
            self.vulInfo.vulDiscoverDate = tdElement.text

        elif u"CVE编号"==detailItemName:            
            self.vulInfo.vulCVE = tdElement.text

        elif u"BUGTRAQ"==detailItemName:            
            self.vulInfo.vulBugTraq = tdElement.text

        elif u"CNNVD编号"==detailItemName:            
            self.vulInfo.vulCNNVD = tdElement.text

        elif u"CNCVE编号"==detailItemName:            
            self.vulInfo.vulCNCVE = tdElement.text

        elif u"CVSS评分"==detailItemName:            
            self.vulInfo.vulCVSS = float(tdElement.text)

        else:
            print(u"没有%s信息" % detailItemName)
    

   