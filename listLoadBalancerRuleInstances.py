#! /usr/bin/python
"""
List all virtual machine instances that are assigned to a load balancer rule.
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

    parser = argparse.ArgumentParser(description="List all virtual machine instances that are assigned to a load balancer rule.")
 
    parser.add_argument("id",help="the ID of the load balancer rule")
    parser.add_argument("--applied",dest="applied",help="true if listing all virtual machines currently applied to the load balancer rule; default is true")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listLoadBalancerRuleInstances"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
