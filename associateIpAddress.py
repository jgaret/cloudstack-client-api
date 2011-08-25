#! /usr/bin/python
"""
Acquires and associates a public IP to an account.
"""
import handleurl.handleurl as hu
import argparse
import pprint
import urllib2
from xml.dom import minidom

if __name__ == "__main__":
    apikey=hu.getenv_apikey()
    secretkey=hu.getenv_secretkey()
    url=hu.getenv_url()

    parser = argparse.ArgumentParser(description="Acquires and associates a public IP to an account.")
 
    parser.add_argument("zoneid",help="the ID of the availability zone you want to acquire an public IP address from")
    parser.add_argument("--account",dest="account",help="the account to associate with this IP address")
    parser.add_argument("--domainid",dest="domainid",help="the ID of the domain to associate with this IP address")
    parser.add_argument("--networkid",dest="networkid",help="The network this ip address should be associated to.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "associateIpAddress"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
