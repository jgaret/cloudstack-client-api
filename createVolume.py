#! /usr/bin/python
"""
Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it.
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

    parser = argparse.ArgumentParser(description="Creates a disk volume from a disk offering. This disk volume must still be attached to a virtual machine to make use of it.")
 
    parser.add_argument("name",help="the name of the disk volume")
    parser.add_argument("--account",dest="account",help="the account associated with the disk volume. Must be used with the domainId parameter.")
    parser.add_argument("--diskofferingid",dest="diskofferingid",help="the ID of the disk offering. Either diskOfferingId or snapshotId must be passed in.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID associated with the disk offering. If used with the account parameter returns the disk volume associated with the account for the specified domain.")
    parser.add_argument("--size",dest="size",help="Arbitrary volume size. Mutually exclusive with diskOfferingId")
    parser.add_argument("--snapshotid",dest="snapshotid",help="the snapshot ID for the disk volume. Either diskOfferingId or snapshotId must be passed in.")
    parser.add_argument("--zoneid",dest="zoneid",help="the ID of the availability zone")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createVolume"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
