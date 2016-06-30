#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import time
from datetime import date, timedelta
import re

import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename= str(date.today()) + '.log',
                filemode='w')


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat',
    'Referer': 'http://dsmis.szsfm.com/WeiXin/Student/Home.aspx?code=0013qKeo1r4Vuw0gOKgo18yGeo13qKex&state=gh_5151a34f78a2',
}

def login():
    url = 'http://dsmis.szsfm.com/WeiXin/Student/StuLogin.aspx?wx=gh_5151a34f78a2&openId=ojiehs8aTZ_lx4TQmOZt-HKsovbo&back=%2fWeiXin%2fStudent%2fHome.aspx%3fcode%3d011oQHWj1mmhuz0By8Vj19vEWj1oQHWY%26state%3dgh_5151a34f78a2'
    login_data = {
        '__LASTFOCUS':'',
        '__VIEWSTATE': '/wEPDwUKLTc1MTg1MzgwNA9kFgICAw9kFgQCAQ8PFgIeCEltYWdlVXJsBS9odHRwOi8vZHNtaXMuc3pzZm0uY29tL1NjaG9vbEltYWdlLzAxMHNtYWxsLnBuZ2RkAhEPDxYCHgRUZXh0BTbmt7HlnLPluILlkInpobrovr7mnLrliqjovabpqb7pqbblkZjln7norq3mnInpmZDlhazlj7hkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUOY2hrUmVtZW1iZXJQd2SrQHKtb7KWV0BBjss5dJiIPeQnViMGguXU8q7QhynQ6Q==',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__EVENTVALIDATION': '/wEWBwKUxJORCgKl1bKzCQK1qbSRCwKw8v7wBgKO3rnoDQLl1Z2cDwK128WQASvDJXDkC7cYOt/TXYFwsQNkrsRriQ6sz9V2R6CAGOdA',
        'txtUserName': '18316997339',
        'txtPassword': '974837',
        'hdnWxUserId': 'ojiehs8aTZ_lx4TQmOZt-HKsovbo',
        'btnBinding': '登录系统',
        'hdnWeiXinNo': 'gh_5151a34f78a2'
    }
    res = requests.post(url, data=login_data, headers=headers)
    return res




def getSchedule(headers):
    logging.debug('getSchedule start ============')
    tomorrow = getTomorrow()
    url = 'http://dsmis.szsfm.com/WeiXin/Student/ScheduleList.aspx?&LoadAjaxData=LoadTime&coachId=9DA23C7A-E3BA-4025-9FC1-1BA63C32D364&date='+ tomorrow +'&id=0.039887798484414816'
    res = requests.get(url, headers=headers)
    text = res.text
    logging.debug('getSchedule end ============')

    logging.debug('getSchedule text ============' + text)

    m = re.search(r'SelectTime\(.*\)', text)

    if m:
        schedule = re.sub("'", "", m.group(0).split(',')[1].split(')')[0])
        return schedule
    else:
        return None

def addOrder(headers, schedule):
    url = 'http://dsmis.szsfm.com/WeiXin/Student/AddOrder.aspx'
    data = {
        '__VIEWSTATE': '/wEPDwULLTE1MTc1Njc5MzJkZBLtAqFGVYBX8PpCxXSD9dgCj0ULY0Frt8UC67AEmCle',
        '__EVENTVALIDATION': '/wEWDQKhtd7OAQKP0OeuBgK9mbPjAwKA+7SWBAKi2b28AgLlicSCDgL5h+3dBgKct7iSDAL4p/7IAgKJ3pHHDQLypMGrDQKP3rHHDQKv3bT4B3TecrEr7N9zqQLRg6tPiujiY1D96Dr+GFOgDcvhVgep',
        'hidEduSiteId': '2F7FF2A1-C46D-446D-9793-140BBA157DFB',
        'hidTrainId': 'F66AB04A-A986-4D60-9016-D0D0C855322E',
        'hidCoachId': '9DA23C7A-E3BA-4025-9FC1-1BA63C32D364',
        'hidScheduleId': schedule,
        'hidFeesType': '2',
        'hidPrice': '0.00',
        'btnSave': '提交',
        'hidEduSiteName': '西乡',
        'hidTrainName': '科目二训练',
        'hidCoachName': '何道成',
        'hidTrainTime':  getTomorrow() + ' 08:00-09:00',
        'hidOrderMinMinute': '60'
    }
    res = requests.post(url, headers=headers, data=data)

def getCookieFromLogin(res):
    # cookies = []
    headers = login_res.headers
    cookieList = headers['Set-Cookie'].split(',')
    # for cookie in cookieList:
    #     cookies.append(cookie.split(';')[0])
    cookies = cookieList[0].split(';')[0]+ ';' + cookieList[1].split(';')[0]
    return cookies

def getHeaders(cookie=''):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat',
        'Referer': 'http://dsmis.szsfm.com/WeiXin/Student/Home.aspx?code=0013qKeo1r4Vuw0gOKgo18yGeo13qKex&state=gh_5151a34f78a2',
    }
    headers['Cookie'] = cookie
    return headers

def getTomorrow():
    return str(date.today() + timedelta(1))

if __name__ == '__main__':
    #登录

    logging.debug('login start')
    login_res = login()
    logging.debug('login end')

    #从登录结果中拿cookie

    logging.debug('getCookieFromLogin start')
    cookie = getCookieFromLogin(login_res)
    logging.debug('getCookieFromLogin end')

    #生成带cookie的http头部
    logging.debug('getHeaders start')
    headers = getHeaders(cookie=cookie)
    logging.debug('getHeaders end')
    logging.debug('headers: ' + str(headers))
    #拿时间段数据
    while 1:
        schedule = getSchedule(headers)
        if schedule:
            break

    #下订单请求
    while 1:
        logging.debug('addOrder start =============')
        addOrder(headers=headers, skedule=schedule)
        logging.debug('addOrder end =============')


