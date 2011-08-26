#! /usr/bin/python
"""
Creates a port forwarding rule
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

    parser = argparse.ArgumentParser(description="Creates a port forwarding rule")
 
    parser.add_argument("ipaddressid",help="the IP address id of the port forwarding rule")
    parser.add_argument("privateport",help="the starting port of port forwarding rule's private port range")
    parser.add_argument("protocol",help="the protocol for the port fowarding rule. Valid values are TCP or UDP.")
    parser.add_argument("publicport",help="the starting port of port forwarding rule's public port range")
    parser.add_argument("virtualmachineid",help="the ID of the virtual machine for the port forwarding rule")
    parser.add_argument("--cidrlist",dest="cidrlist",help="the cidr list to forward traffic from")
    parser.add_argument("--privateendport",dest="privateendport",help="the ending port of port forwarding rule's private port range")
    parser.add_argument("--publicendport",dest="publicendport",help="the ending port of port forwarding rule's private port range")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createPortForwardingRule"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
