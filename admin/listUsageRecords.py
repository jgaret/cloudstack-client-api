#! /usr/bin/python
"""
Lists usage records for accounts
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

    parser = argparse.ArgumentParser(description="Lists usage records for accounts")
 
    parser.add_argument("enddate",help="End date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-03.")
    parser.add_argument("startdate",help="Start date range for usage record query. Use yyyy-MM-dd as the date format, e.g. startDate=2009-06-01.")
    parser.add_argument("--account",dest="account",help="List usage records for the specified user.")
    parser.add_argument("--accountid",dest="accountid",help="List usage records for the specified account")
    parser.add_argument("--domainid",dest="domainid",help="List usage records for the specified domain.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listUsageRecords"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
