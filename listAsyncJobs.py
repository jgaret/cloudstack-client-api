#! /usr/bin/python
"""
Lists all pending asynchronous jobs for the account.
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

    parser = argparse.ArgumentParser(description="Lists all pending asynchronous jobs for the account.")
 
    parser.add_argument("--account",dest="account",help="the account associated with the async job. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID associated with the async job.  If used with the account parameter, returns async jobs for the account in the specified domain.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--startdate",dest="startdate",help="the start date of the async job")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listAsyncJobs"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
