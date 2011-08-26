#! /usr/bin/python
"""
Creates an ip forwarding rule
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

    parser = argparse.ArgumentParser(description="Creates an ip forwarding rule")
 
    parser.add_argument("ipaddressid",help="the public IP address id of the forwarding rule, already associated via associateIp")
    parser.add_argument("protocol",help="the protocol for the rule. Valid values are TCP or UDP.")
    parser.add_argument("startport",help="the start port for the rule")
    parser.add_argument("--endport",dest="endport",help="the end port for the rule")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createIpForwardingRule"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
