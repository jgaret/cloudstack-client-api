#! /usr/bin/python
"""
Creates a disk offering.
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

    parser = argparse.ArgumentParser(description="Creates a disk offering.")
 
    parser.add_argument("displaytext",help="alternate display text of the disk offering")
    parser.add_argument("name",help="name of the disk offering")
    parser.add_argument("--customized",dest="customized",help="whether disk offering is custom or not")
    parser.add_argument("--disksize",dest="disksize",help="size of the disk offering in GB")
    parser.add_argument("--domainid",dest="domainid",help="the ID of the containing domain, null for public offerings")
    parser.add_argument("--tags",dest="tags",help="tags for the disk offering")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createDiskOffering"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
