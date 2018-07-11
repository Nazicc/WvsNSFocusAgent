#/usr/bin/env python
# -*- coding: UTF-8 -*-
import time

from app.config import loginInfo,baseInfo
from app.xpath import *


def login(browser):
    print(baseInfo["wvssServerUrl"])
    browser.get(baseInfo["wvssServerUrl"])
    browser.find_element_by_xpath(loginInfoXpath["username_xpath"]).send_keys(loginInfo["username"])
    browser.find_element_by_xpath(loginInfoXpath["password_xpath"]).send_keys(loginInfo["password"])
    time.sleep(1)
    browser.find_element_by_xpath(loginInfoXpath["login_xpath"]).click()
    time.sleep(2)

