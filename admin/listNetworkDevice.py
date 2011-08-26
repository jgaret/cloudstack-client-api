#! /usr/bin/python
"""
List network device.
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

    parser = argparse.ArgumentParser(description="List network device.")
 
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--networkdeviceparameterlist",dest="networkdeviceparameterlist",help="parameters for network device")
    parser.add_argument("--networkdevicetype",dest="networkdevicetype",help="Network device type, now supports ExternalDhcp, ExternalFirewall, ExternalLoadBalancer, PxeServer")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listNetworkDevice"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
