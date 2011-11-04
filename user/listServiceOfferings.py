#! /usr/bin/python
"""
Lists all available service offerings.
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

    parser = argparse.ArgumentParser(description="Lists all available service offerings.")
 
    parser.add_argument("--domainid",dest="domainid",help="the ID of the domain associated with the service offering")
    parser.add_argument("--id",dest="id",help="ID of the service offering")
    parser.add_argument("--issystem",dest="issystem",help="is this a system vm offering")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="name of the service offering")
    parser.add_argument("--systemvmtype",dest="systemvmtype",help="the system VM type. Possible types are 'consoleproxy', 'secondarystoragevm' or 'domainrouter'.")
    parser.add_argument("--virtualmachineid",dest="virtualmachineid",help="the ID of the virtual machine. Pass this in if you want to see the available service offering that a virtual machine can be changed to.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listServiceOfferings"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
