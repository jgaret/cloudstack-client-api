#! /usr/bin/python
"""
Lists load balancer rules.
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

    parser = argparse.ArgumentParser(description="Lists load balancer rules.")
 
    parser.add_argument("--account",dest="account",help="the account of the load balancer rule. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID of the load balancer rule. If used with the account parameter, lists load balancer rules for the account in the specified domain.")
    parser.add_argument("--id",dest="id",help="the ID of the load balancer rule")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="the name of the load balancer rule")
    parser.add_argument("--publicipid",dest="publicipid",help="the public IP address id of the load balancer rule")
    parser.add_argument("--virtualmachineid",dest="virtualmachineid",help="the ID of the virtual machine of the load balancer rule")
    parser.add_argument("--zoneid",dest="zoneid",help="the availability zone ID")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listLoadBalancerRules"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
