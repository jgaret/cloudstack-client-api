#! /usr/bin/python
"""
Lists all available snapshots for the account.
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

    parser = argparse.ArgumentParser(description="Lists all available snapshots for the account.")
 
    parser.add_argument("--account",dest="account",help="lists snapshot belongig to the specified account. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID. If used with the account parameter, lists snapshots for the specified account in this domain.")
    parser.add_argument("--id",dest="id",help="lists snapshot by snapshot ID")
    parser.add_argument("--intervaltype",dest="intervaltype",help="valid values are HOURLY, DAILY, WEEKLY, and MONTHLY.")
    parser.add_argument("--isrecursive",dest="isrecursive",help="defaults to false, but if true, lists all snapshots from the parent specified by the domain id till leaves.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="lists snapshot by snapshot name")
    parser.add_argument("--snapshottype",dest="snapshottype",help="valid values are MANUAL or RECURRING.")
    parser.add_argument("--volumeid",dest="volumeid",help="the ID of the disk volume")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listSnapshots"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
