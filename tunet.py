#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import httplib
import urllib
import md5
import time


tunet_addr = 'net.tsinghua.edu.cn'
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}


def check_status():
    conn = httplib.HTTPConnection(tunet_addr)
    body = urllib.urlencode({
        'action': 'check_online',
    })
    conn.request('POST', '/do_login.php', body, headers)
    resp = conn.getresponse().read()
    conn.close()
    return resp


def login(username, password):
    conn = httplib.HTTPConnection(tunet_addr)
    body = urllib.urlencode({
        'action': 'login',
        'username': username,
        'password': '{MD5_HEX}' + md5.new(password).hexdigest(),
        'ac_id': 1
    })
    conn.request('POST', '/do_login.php', body, headers)
    resp = conn.getresponse().read()
    conn.close()
    return resp


def logout():
    conn = httplib.HTTPConnection(tunet_addr)
    body = urllib.urlencode({
        'action': 'logout',
    })
    conn.request('POST', '/do_login.php', body, headers)
    resp = conn.getresponse().read()
    conn.close()
    return resp


if __name__ == "__main__":
    print check_status()
