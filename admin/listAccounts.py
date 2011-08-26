#! /usr/bin/python
"""
Lists accounts and provides detailed account information for listed accounts
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

    parser = argparse.ArgumentParser(description="Lists accounts and provides detailed account information for listed accounts")
 
    parser.add_argument("--accounttype",dest="accounttype",help="list accounts by account type. Valid account types are 1 (admin), 2 (domain-admin), and 0 (user).")
    parser.add_argument("--domainid",dest="domainid",help="list all accounts in specified domain. If used with the name parameter, retrieves account information for the account with specified name in specified domain.")
    parser.add_argument("--id",dest="id",help="list account by account ID")
    parser.add_argument("--iscleanuprequired",dest="iscleanuprequired",help="list accounts by cleanuprequred attribute (values are true or false)")
    parser.add_argument("--isrecursive",dest="isrecursive",help="defaults to false, but if true, lists all accounts from the parent specified by the domain id till leaves.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="list account by account name")
    parser.add_argument("--state",dest="state",help="list accounts by state. Valid states are enabled, disabled, and locked.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listAccounts"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
