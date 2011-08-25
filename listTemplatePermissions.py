#! /usr/bin/python
"""
List template visibility and all accounts that have permissions to view this template.
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

    parser = argparse.ArgumentParser(description="List template visibility and all accounts that have permissions to view this template.")
 
    parser.add_argument("id",help="the template ID")
    parser.add_argument("--account",dest="account",help="List template visibility and permissions for the specified account. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="List template visibility and permissions by domain. If used with the account parameter, specifies in which domain the specified account exists.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listTemplatePermissions"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
