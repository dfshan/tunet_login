#!/usr/bin/env python2.7
import httplib

if __name__ == '__main__':
    conn = httplib.HTTPConnection('166.111.8.120')
    conn.request('post', '/cgi-bin/do_logout')
    resp = conn.getresponse().read()
    print resp
    conn.close()
