#! /usr/bin/python
"""
Creates a load balancer rule
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

    parser = argparse.ArgumentParser(description="Creates a load balancer rule")
 
    parser.add_argument("algorithm",help="load balancer algorithm (source, roundrobin, leastconn)")
    parser.add_argument("name",help="name of the load balancer rule")
    parser.add_argument("privateport",help="the private port of the private ip address/virtual machine where the network traffic will be load balanced to")
    parser.add_argument("publicipid",help="public ip address id from where the network traffic will be load balanced from")
    parser.add_argument("publicport",help="the public port from where the network traffic will be load balanced from")
    parser.add_argument("--description",dest="description",help="the description of the load balancer rule")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createLoadBalancerRule"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
