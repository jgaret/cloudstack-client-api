#! /usr/bin/python
"""
Creates a network
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

    parser = argparse.ArgumentParser(description="Creates a network")
 
    parser.add_argument("displaytext",help="the display text of the network")
    parser.add_argument("name",help="the name of the network")
    parser.add_argument("networkofferingid",help="the network offering id")
    parser.add_argument("zoneid",help="the Zone ID for the network")
    parser.add_argument("--account",dest="account",help="account who will own the network")
    parser.add_argument("--domainid",dest="domainid",help="domain ID of the account owning a network")
    parser.add_argument("--endip",dest="endip",help="the ending IP address in the network IP range. If not specified, will be defaulted to startIP")
    parser.add_argument("--gateway",dest="gateway",help="the gateway of the network")
    parser.add_argument("--isdefault",dest="isdefault",help="true if network is default, false otherwise")
    parser.add_argument("--isshared",dest="isshared",help="true is network is shared across accounts in the Zone")
    parser.add_argument("--netmask",dest="netmask",help="the netmask of the network")
    parser.add_argument("--networkdomain",dest="networkdomain",help="network domain")
    parser.add_argument("--startip",dest="startip",help="the beginning IP address in the network IP range")
    parser.add_argument("--tags",dest="tags",help="Tag the network")
    parser.add_argument("--vlan",dest="vlan",help="the ID or VID of the network")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createNetwork"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
