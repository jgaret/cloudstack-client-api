#! /usr/bin/python
"""
Lists all available network offerings.
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

    parser = argparse.ArgumentParser(description="Lists all available network offerings.")
 
    parser.add_argument("--availability",dest="availability",help="the availability of network offering. Default value is Required")
    parser.add_argument("--displaytext",dest="displaytext",help="list network offerings by display text")
    parser.add_argument("--guestiptype",dest="guestiptype",help="the guest ip type for the network offering, supported types are Direct and Virtual.")
    parser.add_argument("--id",dest="id",help="list network offerings by id")
    parser.add_argument("--isdefault",dest="isdefault",help="true if need to list only default network offerings. Default value is false")
    parser.add_argument("--isshared",dest="isshared",help="true is network offering supports vlans")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="list network offerings by name")
    parser.add_argument("--specifyvlan",dest="specifyvlan",help="the tags for the network offering.")
    parser.add_argument("--traffictype",dest="traffictype",help="list by traffic type")
    parser.add_argument("--zoneid",dest="zoneid",help="list netowrk offerings available for network creation in specific zone")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listNetworkOfferings"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
