#! /usr/bin/python
"""
Lists all public ip addresses
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

    parser = argparse.ArgumentParser(description="Lists all public ip addresses")
 
    parser.add_argument("--account",dest="account",help="lists all public IP addresses by account. Must be used with the domainId parameter.")
    parser.add_argument("--allocatedonly",dest="allocatedonly",help="limits search results to allocated public IP addresses")
    parser.add_argument("--domainid",dest="domainid",help="lists all public IP addresses by domain ID. If used with the account parameter, lists all public IP addresses by account for specified domain.")
    parser.add_argument("--forvirtualnetwork",dest="forvirtualnetwork",help="the virtual network for the IP address")
    parser.add_argument("--id",dest="id",help="lists ip address by id")
    parser.add_argument("--ipaddress",dest="ipaddress",help="lists the specified IP address")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--vlanid",dest="vlanid",help="lists all public IP addresses by VLAN ID")
    parser.add_argument("--zoneid",dest="zoneid",help="lists all public IP addresses by Zone ID")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listPublicIpAddresses"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
