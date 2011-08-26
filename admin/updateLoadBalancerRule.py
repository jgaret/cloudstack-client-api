#! /usr/bin/python
"""
Updates load balancer
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

    parser = argparse.ArgumentParser(description="Updates load balancer")
 
    parser.add_argument("id",help="the id of the load balancer rule to update")
    parser.add_argument("--algorithm",dest="algorithm",help="load balancer algorithm (source, roundrobin, leastconn)")
    parser.add_argument("--description",dest="description",help="the description of the load balancer rule")
    parser.add_argument("--name",dest="name",help="the name of the load balancer rule")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateLoadBalancerRule"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
