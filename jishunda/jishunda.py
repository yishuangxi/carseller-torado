import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat',
    'Referer': 'http://dsmis.szsfm.com/WeiXin/Student/Home.aspx?code=041b2RUE0Dyv072H0qSE0hUWUE0b2RUE&state=gh_5151a34f78a2',
    'Cookie': 'ASP.NET_SessionId=ht1gfkide3jzjmlbin5y3knn; LoginCookie=OpenId=ojiehs8aTZ_lx4TQmOZt-HKsovbo&Wx=gh_5151a34f78a2&UserName=18316997339&Password=&RememberPwd=0'
}

url = 'http://dsmis.szsfm.com/WeiXin/Student/AddOrder.aspx'
data = {
    '__VIEWSTATE': '/wEPDwULLTE1MTc1Njc5MzJkZBLtAqFGVYBX8PpCxXSD9dgCj0ULY0Frt8UC67AEmCle',
    '__EVENTVALIDATION': '/wEWDQKhtd7OAQKP0OeuBgK9mbPjAwKA+7SWBAKi2b28AgLlicSCDgL5h+3dBgKct7iSDAL4p/7IAgKJ3pHHDQLypMGrDQKP3rHHDQKv3bT4B3TecrEr7N9zqQLRg6tPiujiY1D96Dr+GFOgDcvhVgep',
    'hidEduSiteId': '2F7FF2A1-C46D-446D-9793-140BBA157DFB',
    'hidTrainId': 'F66AB04A-A986-4D60-9016-D0D0C855322E',
    'hidCoachId': '9DA23C7A-E3BA-4025-9FC1-1BA63C32D364',
    'hidScheduleId':'',
    'hidFeesType': '',
    'hidPrice': ''
}
res = requests.post(url, headers=headers, data=data)

print res.text