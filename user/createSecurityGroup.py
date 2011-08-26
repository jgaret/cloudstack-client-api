#! /usr/bin/python
"""
Creates a security group
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

    parser = argparse.ArgumentParser(description="Creates a security group")
 
    parser.add_argument("name",help="name of the security group")
    parser.add_argument("--account",dest="account",help="an optional account for the security group. Must be used with domainId.")
    parser.add_argument("--description",dest="description",help="the description of the security group")
    parser.add_argument("--domainid",dest="domainid",help="an optional domainId for the security group. If the account parameter is used, domainId must also be used.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createSecurityGroup"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
