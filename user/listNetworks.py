#! /usr/bin/python
"""
Lists all available networks.
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

    parser = argparse.ArgumentParser(description="Lists all available networks.")
 
    parser.add_argument("--account",dest="account",help="account who will own the VLAN. If VLAN is Zone wide, this parameter should be ommited")
    parser.add_argument("--domainid",dest="domainid",help="domain ID of the account owning a VLAN")
    parser.add_argument("--id",dest="id",help="list networks by id")
    parser.add_argument("--isdefault",dest="isdefault",help="true if network is default, false otherwise")
    parser.add_argument("--isshared",dest="isshared",help="true if network is shared across accounts in the Zone, false otherwise")
    parser.add_argument("--issystem",dest="issystem",help="true if network is system, false otherwise")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--traffictype",dest="traffictype",help="type of the traffic")
    parser.add_argument("--type",dest="type",help="the type of the network")
    parser.add_argument("--zoneid",dest="zoneid",help="the Zone ID of the network")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listNetworks"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
