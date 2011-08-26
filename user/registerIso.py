#! /usr/bin/python
"""
Registers an existing ISO into the Cloud.com Cloud.
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

    parser = argparse.ArgumentParser(description="Registers an existing ISO into the Cloud.com Cloud.")
 
    parser.add_argument("displaytext",help="the display text of the ISO. This is usually used for display purposes.")
    parser.add_argument("name",help="the name of the ISO")
    parser.add_argument("url",help="the URL to where the ISO is currently being hosted")
    parser.add_argument("zoneid",help="the ID of the zone you wish to register the ISO to.")
    parser.add_argument("--account",dest="account",help="an optional account name. Must be used with domainId.")
    parser.add_argument("--bootable",dest="bootable",help="true if this ISO is bootable")
    parser.add_argument("--domainid",dest="domainid",help="an optional domainId. If the account parameter is used, domainId must also be used.")
    parser.add_argument("--isextractable",dest="isextractable",help="true if the iso or its derivatives are extractable; default is true")
    parser.add_argument("--isfeatured",dest="isfeatured",help="true if you want this ISO to be featured")
    parser.add_argument("--ispublic",dest="ispublic",help="true if you want to register the ISO to be publicly available to all users, false otherwise.")
    parser.add_argument("--ostypeid",dest="ostypeid",help="the ID of the OS Type that best represents the OS of this ISO")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "registerIso"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
