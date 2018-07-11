#!/usr/bin/env python
#coding:utf-8
# 报表导出菜单
reportExportXpath = '//*[@id="two03"]'

xpathReportExportConfig = {
    'task':'//*[@id="tasks"]',
    'reportName':'//*[@id="reportName"]',

    'reportContentSummary':'//*[@id="summary_report"]',
    'reportCOntentSingleSite':'//*[@id="single_site_report"]',
    
    'riskLevelH':'//*[@id="h_risk"]',
    'riskLevelM':'//*[@id="m_risk"]',
    'riskLevelL':'//*[@id="l_risk"]',

    'reportTemplate':'//*[@id="reportTemplate"]',

    'reportTypeDoc':'//*[@id="reportType1"]',
    'reportTypeHtml':'//*[@id="reportType2"]',
    'reportTypePdf':'//*[@id="reportType3"]',
    'reportTypeXml':'//*[@id="reportType4"]',
    'reportTypeXls':'//*[@id="reportType5"]',
    'reportCreate':'//*[@id="exportReport"]'
}
xpathTaskSelector = '//*[@id="tasks"]'