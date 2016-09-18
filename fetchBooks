# coding:utf8
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import xlsxwriter
import xlrd
import os
from threading import Thread


def getUrl(pageSource, url):
    time.sleep(5)
    soup = BeautifulSoup(pageSource, 'lxml')
    sum = soup.select(".trStyle tbody tr td a")
    for item in sum:
        # print len(item)
        # print item.attrs['href']
        url.append(item.attrs['href'])


def handleRes(source, sheet, row):
    soup = BeautifulSoup(source, 'lxml')
    res = soup.select(".trStyle tbody tr td")
    content = [item.text.strip() for item in res]
    for m in xrange(len(content)):
        sheet.write(row, m, content[m])


def handleItem(name):
    driver = webdriver.PhantomJS()
    driver.get(
        "http://www.gapp.gov.cn/zongshu/serviceListcip.shtml?CIPNum=&ISBN=&Certificate=5%E5%B9%B4%E4%B8%AD%E8%80%833%E5%B9%B4%E6%A8%A1%E6%8B%9F&PublishingUnit=&ValidateCode=WTEL")
    driver.maximize_window()
    try:
        listUrl = []
        if not os.path.exists("%s.xlsx" % name):

            time.sleep(5)
            driver.find_element_by_id("certificate").clear()
            driver.find_element_by_id("certificate").send_keys(name)

            bs = BeautifulSoup(driver.page_source, 'lxml')
            code = bs.select("#ss")[0].text
            driver.find_element_by_id("ValidateCode").send_keys(code)
            driver.find_element_by_id("filessearch").click()
            time.sleep(5)

            ######################################################
            while True:
                print 'loop start'
                try:
                    print 'get next page and url'
                    getUrl(driver.page_source, listUrl)
                    nextPage = driver.find_element_by_link_text(u'下一页')
                    if nextPage and nextPage.is_enabled():
                        nextPage.click()
                        time.sleep(5)
                        print "_________________________________"
                    else:
                        # getUrl(driver.page_source, listUrl)
                        break
                        # nextPage = driver.find_element_by_link_text(u'下一页')
                except:
                    break
            if len(listUrl) != 0:
                workbook = xlsxwriter.Workbook('%s.xlsx' % name)
                worksheet = workbook.add_worksheet(name)
                print u"有%d条数据"%len(listUrl)
                row = 0
                for item in listUrl:
                    driver.get("http://www.gapp.gov.cn" + item)
                    time.sleep(5)
                    print item
                    print "starting》》》》》"
                    handleRes(driver.page_source, worksheet, row)
                    row = row + 1
                workbook.close()
        else:
            print "exists"

    finally:
        driver.quit()


def getContent(m, n, ws):
    for i in range(m, n):
        if i > 0:
            print u"第%s行" % i
            value = ws.cell(i, 0).value
            print value
            handleItem(value)


if __name__ == "__main__":
    workbook = xlrd.open_workbook('senior.xlsx')
    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows
    threadList = []
    a1 = Thread(target=getContent, args=(1, 51, sheet))
    a2 = Thread(target=getContent, args=(51, 100, sheet))
    a3 = Thread(target=getContent, args=(100, 150, sheet))
    a4 = Thread(target=getContent, args=(150, 200, sheet))
    a5 = Thread(target=getContent, args=(200, 250, sheet))
    a6 = Thread(target=getContent, args=(250, 300, sheet))
    a7 = Thread(target=getContent, args=(300, 350, sheet))
    a8 = Thread(target=getContent, args=(350, 400, sheet))
    a9 = Thread(target=getContent, args=(400, 450, sheet))
    a10 = Thread(target=getContent, args=(450, 500, sheet))
    a11 = Thread(target=getContent, args=(500, 550, sheet))

    threadList.append(a1)
    threadList.append(a2)
    threadList.append(a3)
    threadList.append(a4)
    threadList.append(a5)
    threadList.append(a6)
    threadList.append(a7)
    threadList.append(a8)
    threadList.append(a9)
    threadList.append(a10)
    threadList.append(a11)
    for item in threadList:
        item.start()
    for item in threadList:
        item.join()
        #
        # for i in xrange(rows):
        #     if i > 0:
        #         print u"第%s行"%i
        #         value=sheet.cell(i,0).value
        #         print value
        #         handleItem(value)
