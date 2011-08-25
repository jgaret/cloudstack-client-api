#! /usr/bin/python
"""
A command to list events.
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

    parser = argparse.ArgumentParser(description="A command to list events.")
 
    parser.add_argument("--account",dest="account",help="the account for the event. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID for the event. If used with the account parameter, returns all events for an account in the specified domain ID.")
    parser.add_argument("--duration",dest="duration",help="the duration of the event")
    parser.add_argument("--enddate",dest="enddate",help="the end date range of the list you want to retrieve (use format "yyyy-MM-dd" or the new format "yyyy-MM-dd HH:mm:ss")")
    parser.add_argument("--entrytime",dest="entrytime",help="the time the event was entered")
    parser.add_argument("--id",dest="id",help="the ID of the event")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--level",dest="level",help="the event level (INFO, WARN, ERROR)")
    parser.add_argument("--startdate",dest="startdate",help="the start date range of the list you want to retrieve (use format "yyyy-MM-dd" or the new format "yyyy-MM-dd HH:mm:ss")")
    parser.add_argument("--type",dest="type",help="the event type (see event types)")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listEvents"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
