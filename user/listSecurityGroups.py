#! /usr/bin/python
"""
Lists security groups
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

    parser = argparse.ArgumentParser(description="Lists security groups")
 
    parser.add_argument("--account",dest="account",help="lists all available port security groups for the account. Must be used with domainID parameter")
    parser.add_argument("--domainid",dest="domainid",help="lists all available security groups for the domain ID. If used with the account parameter, lists all available security groups for the account in the specified domain ID.")
    parser.add_argument("--id",dest="id",help="list the security group by the id provided")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--securitygroupname",dest="securitygroupname",help="lists security groups by name")
    parser.add_argument("--virtualmachineid",dest="virtualmachineid",help="lists security groups by virtual machine id")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listSecurityGroups"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
