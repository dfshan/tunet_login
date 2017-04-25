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
    config_fname = "tunet.conf"
    parser = argparse.ArgumentParser(
        description="Login to tsinghua network."
    )
    parser.add_argument(
        "-u", "--username", help="Username"
    )
    parser.add_argument(
        "-p", "--password", help="password"
    )
    args = parser.parse_args()
    cf = ConfigParser.ConfigParser()
    cf.read(config_fname)
    status = tunet.check_status()
    if status == "online":
        print tunet.logout()
    if args.username is not None and args.password is not None:
        print "Login using username " + args.username
        print tunet.login(args.username, args.password)
    try:
        username = cf.get("account", "username")
        password = cf.get("account", "password")
    except ConfigParser.NoSectionError, ConfigParser.NoOptionError:
        print ("Please specify username and password either via cmd argument"
               "or in configuration file " + config_fname)
    else:
        print "Login using username " + username
        print tunet.login(username, password)



if __name__ == '__main__':
    main()
