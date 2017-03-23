import time
from sys import exit
from hashlib import sha512
import urllib
from urllib2 import *


for i in range(1,20):
    url="http://wargame.kr:8080/pyc_decompile/"
    seed = time.strftime('%m/%d/HJEJSH', time.localtime());
    hs=sha512(seed).hexdigest();
    t = time.localtime(time.time());
    start = (t.tm_hour %3 + 1);
    end = start * ((t.tm_min+i)%30 + 10);
    ok=hs[start:end];
    
    print "start : " + str(start);
    print "end : " + str(end);
    print "seed : "+ seed;
    print "hs : " + hs;
    print "flag : " + ok;
    print ""; print t;
    print "";

    url += "?flag="+ok
    req = Request(url)
    req.add_header("Cookie","ci_session=a%3A10%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22b8703801b64f9aa21cc03c06518fee62%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22118.221.173.47%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A108%3A%22Mozilla%2F5.0+%28Windows+NT+6.1%3B+WOW64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F56.0.2924.87+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1490248631%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22name%22%3Bs%3A10%3A%22kawa1lg1rl%22%3Bs%3A5%3A%22email%22%3Bs%3A18%3A%22bdb01113%40gmail.com%22%3Bs%3A4%3A%22lang%22%3Bs%3A3%3A%22eng%22%3Bs%3A11%3A%22achievement%22%3Bs%3A7%3A%22default%22%3Bs%3A5%3A%22point%22%3Bs%3A4%3A%226900%22%3B%7Dc50665bce028bd7fbbb4efadf6f39c32d175b9fa")
    req.add_header("User-Agent", "chrome~")

    op = urlopen(req)
    rd = op.read()

    print "Response : " + rd; print " ============== "
