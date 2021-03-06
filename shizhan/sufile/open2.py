# -*- coding:utf-8 -*-

# 通过代理刷点击量
import urllib2
import urllib
import random
import time
import re
from socket import error as SocketError
from cookielib import CookieJar
import socket
import socks
import requests
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1018)
socket.socket = socks.socksocket


class REFRESH:
    def __init__(self):

        self.baseUrl = 'http://www.sufile.com/downcode.php'
        self.downUrl = 'http://www.sufile.com/dd.php?file_key=5f05c94cd4847078&p=0'


        self.user_agents = [
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+',
            'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+',
            'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)',
            'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        ]


    # 打开页面
    def refreshPage(self, ip):
        try:


            # print 'ip ------ ' + ip
            # user_agent = random.choice(self.user_agents)
            proxy = urllib2.ProxyHandler({'http':'http://210.101.131.231:8088'})
            # opener = urllib2.build_opener(proxy)

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1",port=1080)
            # socket.socket = socks.socksocket


            opener.addheaders = [
                ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                # ('Accept-Encoding', 'gzip, deflate, sdch'),
                ('Accept-Language','zh-CN,zh;q=0.8,en;q=0.6'),
                ('Cache-Control', 'max-age=0'),
                ('Connection', 'keep-alive'),
                ('Upgrade-Insecure-Requests', '1'),
                ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'),
                ('Host','page4.dix3.com'),
                ('Referer','http://page4.dix3.com/file/su2266/a5ba31f3/'),
                ('DNT','1')
            ]


            r = opener.open('http://page4.dix3.com/file/su2266/a5ba31f3/', timeout=10)
            d = r.read()
            print d
            with open('./1.html', 'wb') as f:
                f.write(d)

            c = opener.open('http://page4.dix3.com/verifyimg/getPcv.html', timeout=10)
            with open('./code2.jpg', 'wb') as f:
                f.write(c.read())


            code = raw_input('input code:')

            self.getDown(ip, code, opener)

        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False

        return True


    def getDown(self, ip, code, opener):
        try:

            # url = 'http://www.baidu.com'
            url = 'http://page4.dix3.com/file/down/su2266/a5ba31f3/'+code+'.html'

            print url
            r = opener.open(url, timeout=10)
            d = r.read()

            with open('down.html', 'wb') as f:
                f.write(d)




        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False

        return True



    def getResult(self, ip, cookieHandle, fileID):
        try:

            user_agent = random.choice(self.user_agents)
            proxy = urllib2.ProxyHandler({'http':''+ ip +''})
            opener = urllib2.build_opener(proxy)
            opener.addheaders = [
                ('User_agent',user_agent),
                ('Referer','http://www.sufile.com/down/'+fileID+'.html'),
                ('Host','www.sufile.com'),
                ('DNT','1')
            ]

            opener = urllib2.build_opener(cookieHandle)
            r = opener.open('http://www.sufile.com/dd.php?file_key='+fileID+'&p=0', timeout=10)
            d = r.read()

            with open('./result.html', 'wb') as f:
                f.write(d)


            p = re.compile('<a id="downs" href="(.*?)"', re.S)
            r = re.search(p, d)
            print r.group(1).strip()


        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False

        return True



refresh = REFRESH()
refresh.refreshPage('199.115.117.212')
# proxies = {'http': "socks5://127.0.0.1:1080"}
# d = requests.get('http://www.google.com', proxies=proxies)
# print d
