o = {
    'X-Via': '1.1hnwap224.162: 3800(CdnCacheServerV2.0)',
    'X-AspNet-Version': '4.0.30319',
    'Transfer-Encoding': 'chunked',
    'Set-Cookie': 'ASP.NET_SessionId=iddaesiv1la5zrequxdvpqnq;path=/;HttpOnly,LoginCookie=OpenId=ojiehs8aTZ_lx4TQmOZt-HKsovbo&Wx=gh_5151a34f78a2&UserName=18316997339&Password=&RememberPwd=0;expires=Sun,25-Jun-201708: 33: 12GMT;path=/,LoginCookie=OpenId=ojiehs8aTZ_lx4TQmOZt-HKsovbo&Wx=gh_5151a34f78a2&UserName=18316997339&Password=&RememberPwd=0;expires=Sun,25-Jun-201708: 33: 12GMT;path=/,LoginCookie=OpenId=ojiehs8aTZ_lx4TQmOZt-HKsovbo&Wx=gh_5151a34f78a2&UserName=18316997339&Password=&RememberPwd=0;expires=Sun,25-Jun-201708: 33: 12GMT;path=/,LoginCookie=OpenId=ojiehs8aTZ_lx4TQmOZt-HKsovbo&Wx=gh_5151a34f78a2&UserName=18316997339&Password=&RememberPwd=0;expires=Sun,25-Jun-201708: 33: 12GMT;path=/,LoginCookie=OpenId=ojiehs8aTZ_lx4TQmOZt-HKsovbo&Wx=gh_5151a34f78a2&UserName=18316997339&Password=&RememberPwd=0;expires=Sun,25-Jun-201708: 33: 12GMT;path=/',
    'X-Powered-By': 'ASP.NET',
    'Server': 'Microsoft-IIS/6.0',
    'Connection': 'keep-alive',
    'Cache-Control': 'private',
    'Date': 'Sat,25Jun201608: 33: 12GMT',
    'Content-Type': 'text/html;charset=utf-8'
}

cookies = o['Set-Cookie'].split(',')

for cookie in cookies:
    print cookie