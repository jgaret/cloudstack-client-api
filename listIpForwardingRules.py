#! /usr/bin/python
"""
List the ip forwarding rules
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

    parser = argparse.ArgumentParser(description="List the ip forwarding rules")
 
    parser.add_argument("--account",dest="account",help="the account associated with the ip forwarding rule. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="Lists all rules for this id. If used with the account parameter, returns all rules for an account in the specified domain ID.")
    parser.add_argument("--id",dest="id",help="Lists rule with the specified ID.")
    parser.add_argument("--ipaddressid",dest="ipaddressid",help="list the rule belonging to this public ip address")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--virtualmachineid",dest="virtualmachineid",help="Lists all rules applied to the specified Vm.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listIpForwardingRules"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
