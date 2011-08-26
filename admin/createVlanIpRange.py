#! /usr/bin/python
"""
Creates a VLAN IP range.
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

    parser = argparse.ArgumentParser(description="Creates a VLAN IP range.")
 
    parser.add_argument("startip",help="the beginning IP address in the VLAN IP range")
    parser.add_argument("--account",dest="account",help="account who will own the VLAN. If VLAN is Zone wide, this parameter should be ommited")
    parser.add_argument("--domainid",dest="domainid",help="domain ID of the account owning a VLAN")
    parser.add_argument("--endip",dest="endip",help="the ending IP address in the VLAN IP range")
    parser.add_argument("--forvirtualnetwork",dest="forvirtualnetwork",help="true if VLAN is of Virtual type, false if Direct")
    parser.add_argument("--gateway",dest="gateway",help="the gateway of the VLAN IP range")
    parser.add_argument("--netmask",dest="netmask",help="the netmask of the VLAN IP range")
    parser.add_argument("--networkid",dest="networkid",help="the network id")
    parser.add_argument("--podid",dest="podid",help="optional parameter. Have to be specified for Direct Untagged vlan only.")
    parser.add_argument("--vlan",dest="vlan",help="the ID or VID of the VLAN. Default is an "untagged" VLAN.")
    parser.add_argument("--zoneid",dest="zoneid",help="the Zone ID of the VLAN IP range")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createVlanIpRange"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
