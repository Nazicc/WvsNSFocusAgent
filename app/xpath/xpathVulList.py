#/usr/bin/env python
#coding=utf-8

# main 框架
xpathTaskInfoViewSel = {
    'xpathTaskParamViewSel'     : '/html/body/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/a',     #任务参数
    'xpathTaskSummaryViewSel'   : '/html/body/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/a',     #综述信息
    'xpathSiteListViewSel'      : '/html/body/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[3]/a',     #站点列表
    'xpathVulListViewSel'       : '/html/body/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[4]/a',     #漏洞列表
    'xpathOptLogViewSel'        :'/html/body/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[5]/a',      #操作日志
    'xpathRefStandaryViewSel'   : '/html/body/div/table/tbody/tr[1]/td/div/table/tbody/tr/td[6]/a'      #参考标准
}
xpathVulInfoList={
    'vulList'       :   '//*[@id="vulDataTable"]/tbody/tr',
    'vulName'       :   '//*[@id="vulDataTable"]/tbody/tr[{sIndex}]/td[1]',     #sIndex 是奇数从1开始
    'vulTimes'      :   '//*[@id="vulDataTable"]/tbody/tr[{sIndex}]/td[2]',
    # 'vulDetail'   :   '//*[@id="vulDataTable"]/tbody/tr[{{2*i+2}}]',
    'vulDetailRow'  :   '//*[@id="vulDataTable"]/tbody/tr[{mIndex}]/td/table/tbody/tr' #mIndex是偶数，mIndex = sIndex +1
    # 'vulDetailRow'  :   '/html/body/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[2]/div[2]/table/tbody/tr[{mIndex}]/td/table/tbody/tr'    
}
# 每一行信息解析
# 为xpathVulInfoList['vulDetailRow']元素组中每一个元素的子元素
xpathVulDetail={
    'detailItemName':'th',
    'detailContent':'td'
}
# 为xpathVulDetail['detailContent']下子元素
xpathVulSiteInfo = {
    'showUrls':'span[2]',
    'vulUrlList':"div",   #在xpathVulDetail['detailContent']元素下的子元素
    'vulSite':'a'
}

