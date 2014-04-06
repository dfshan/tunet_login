#!/usr/bin/env python2.7
import httplib
import urllib
import md5
import time

username = 'put your username here'
password = 'put your password here'

if __name__ == '__main__':
    conn = httplib.HTTPConnection('166.111.8.120')
    headers = {"Connect-type":"application/x-www-form-urlencoded"}
    body = urllib.urlencode({'username':username, 'password':md5.new(password).hexdigest(), 'drop':0, 'type':1, 'n':100})
    conn.request('post', '/cgi-bin/do_login', body, headers)
    resp = conn.getresponse().read()
    while resp == 'ip_exist_error':
        conn.close()
        conn = httplib.HTTPConnection('166.111.8.120')
        conn.request('post', '/cgi-bin/do_logout')
        conn.close()
        time.sleep(2)
        conn = httplib.HTTPConnection('166.111.8.120')
        conn.request('post', '/cgi-bin/do_login', body, headers)
        resp = conn.getresponse().read()
    print resp
    conn.close()
