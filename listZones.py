#! /usr/bin/python
"""
Lists zones
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

    parser = argparse.ArgumentParser(description="Lists zones")
 
    parser.add_argument("--available",dest="available",help="true if you want to retrieve all available Zones. False if you only want to return the Zones from which you have at least one VM. Default is false.")
    parser.add_argument("--domainid",dest="domainid",help="the ID of the domain associated with the zone")
    parser.add_argument("--id",dest="id",help="the ID of the zone")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listZones"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
