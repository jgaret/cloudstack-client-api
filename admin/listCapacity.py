#! /usr/bin/python
"""
Lists capacity.
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

    parser = argparse.ArgumentParser(description="Lists capacity.")
 
    parser.add_argument("--hostid",dest="hostid",help="lists capacity by the Host ID")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--podid",dest="podid",help="lists capacity by the Pod ID")
    parser.add_argument("--type",dest="type",help="lists capacity by type")
    parser.add_argument("--zoneid",dest="zoneid",help="lists capacity by the Zone ID")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listCapacity"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
