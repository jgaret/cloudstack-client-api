#! /usr/bin/python
"""
Lists all VLAN IP ranges.
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

    parser = argparse.ArgumentParser(description="Lists all VLAN IP ranges.")
 
    parser.add_argument("--account",dest="account",help="the account with which the VLAN IP range is associated. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID with which the VLAN IP range is associated.  If used with the account parameter, returns all VLAN IP ranges for that account in the specified domain.")
    parser.add_argument("--forvirtualnetwork",dest="forvirtualnetwork",help="true if VLAN is of Virtual type, false if Direct")
    parser.add_argument("--id",dest="id",help="the ID of the VLAN IP range")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--networkid",dest="networkid",help="network id of the VLAN IP range")
    parser.add_argument("--podid",dest="podid",help="the Pod ID of the VLAN IP range")
    parser.add_argument("--vlan",dest="vlan",help="the ID or VID of the VLAN. Default is an "untagged" VLAN.")
    parser.add_argument("--zoneid",dest="zoneid",help="the Zone ID of the VLAN IP range")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listVlanIpRanges"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
