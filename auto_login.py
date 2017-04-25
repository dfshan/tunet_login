#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import httplib
import urllib
import md5
import time
import tunet
import argparse
import ConfigParser


def main():
    parser = argparse.ArgumentParser(
        description="Login to tsinghua network."
    )
    parser.add_argument(
        "-u", "--username",
        help="Username"
    )
    parser.add_argument(
        "-p", "--password",
        help="password"
    )
    config_fname = "tunet.conf"
    args = parser.parse_args()
    if args.username is not None and args.password is not None:
        username, password = args.username, args.password
    else:
        cf = ConfigParser.ConfigParser()
        cf.read(config_fname)
        status = tunet.check_status()
        try:
            username = cf.get("account", "username")
            password = cf.get("account", "password")
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            print ("Please specify username and password either via cmd argument"
                   "or in configuration file " + config_fname)
            return None
    print "Login using username: " + username
    while True:
        if tunet.check_status() != 'online':
            print tunet.login(username, password)
        time.sleep(11)


if __name__ == '__main__':
    main()
