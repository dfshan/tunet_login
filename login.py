#!/usr/bin/env python2.7
import httplib
import urllib
import md5
import time

username = 'your username'
password = 'your passwork'

if __name__ == '__main__':
    conn = httplib.HTTPConnection('166.111.8.120')
    headers = {"Connect-type":"application/x-www-form-urlencoded"}
    body = urllib.urlencode({'username':username, 'password':md5.new(password).hexdigest(), 'drop':0, 'type':1, 'n':100})
    # print body
    resp = 'ip_exist_error'
    while resp == 'ip_exist_error':
        conn.request('get', '/cgi-bin/do_login', body, headers)
        resp = conn.getresponse().read()
        time.sleep(2)
    conn.close()
