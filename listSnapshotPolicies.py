#! /usr/bin/python
"""
Lists snapshot policies.
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

    parser = argparse.ArgumentParser(description="Lists snapshot policies.")
 
    parser.add_argument("volumeid",help="the ID of the disk volume")
    parser.add_argument("--account",dest="account",help="lists snapshot policies for the specified account. Must be used with domainid parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID. If used with the account parameter, lists snapshot policies for the specified account in this domain.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listSnapshotPolicies"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
