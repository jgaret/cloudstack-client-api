#! /usr/bin/python
"""
Deletes security group
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

    parser = argparse.ArgumentParser(description="Deletes security group")
 
    parser.add_argument("--account",dest="account",help="the account of the security group. Must be specified with domain ID")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID of account owning the security group")
    parser.add_argument("--id",dest="id",help="The ID of the security group. Mutually exclusive with name parameter")
    parser.add_argument("--name",dest="name",help="The ID of the security group. Mutually exclusive with id parameter")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "deleteSecurityGroup"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
