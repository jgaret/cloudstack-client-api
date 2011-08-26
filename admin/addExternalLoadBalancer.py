#! /usr/bin/python
"""
Adds an external load balancer appliance.
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

    parser = argparse.ArgumentParser(description="Adds an external load balancer appliance.")
 
    parser.add_argument("password",help="Password of the external load balancer appliance.")
    parser.add_argument("url",help="URL of the external load balancer appliance.")
    parser.add_argument("username",help="Username of the external load balancer appliance.")
    parser.add_argument("zoneid",help="Zone in which to add the external load balancer appliance.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "addExternalLoadBalancer"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
