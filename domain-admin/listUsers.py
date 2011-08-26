#! /usr/bin/python
"""
Lists user accounts
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

    parser = argparse.ArgumentParser(description="Lists user accounts")
 
    parser.add_argument("--account",dest="account",help="List user by account. Must be used with the domainId parameter.")
    parser.add_argument("--accounttype",dest="accounttype",help="List users by account type. Valid types include admin, domain-admin, read-only-admin, or user.")
    parser.add_argument("--domainid",dest="domainid",help="List all users in a domain. If used with the account parameter, lists an account in a specific domain.")
    parser.add_argument("--id",dest="id",help="List user by ID.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--state",dest="state",help="List users by state of the user account.")
    parser.add_argument("--username",dest="username",help="List user by the username")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listUsers"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
