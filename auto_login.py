#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import httplib
import urllib
import md5
import time
import tunet
import argparse

username = 'put your username here'
password = 'put your password here'


def main():
    parser = argparse.ArgumentParser(
        description="Login to tsinghua network."
    )
    parser.add_argument(
        "-u", "--username", default=username,
        help="Username"
    )
    parser.add_argument(
        "-p", "--password", default=username,
        help="password"
    )
    args = parser.parse_args()
    while True:
        if tunet.check_status() != 'online':
            print tunet.login(args.username, args.password)
        time.sleep(11)


if __name__ == '__main__':
    main()
