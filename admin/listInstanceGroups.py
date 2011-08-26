#! /usr/bin/python
"""
Lists vm groups
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

    parser = argparse.ArgumentParser(description="Lists vm groups")
 
    parser.add_argument("--account",dest="account",help="list instance group belonging to the specified account. Must be used with domainid parameter")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID. If used with the account parameter, lists virtual machines for the specified account in this domain.")
    parser.add_argument("--id",dest="id",help="list instance groups by ID")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="list instance groups by name")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listInstanceGroups"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
