#! /usr/bin/python
"""
Creates an instant snapshot of a volume.
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

    parser = argparse.ArgumentParser(description="Creates an instant snapshot of a volume.")
 
    parser.add_argument("volumeid",help="The ID of the disk volume")
    parser.add_argument("--account",dest="account",help="The account of the snapshot. The account parameter must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="The domain ID of the snapshot. If used with the account parameter, specifies a domain for the account associated with the disk volume.")
    parser.add_argument("--policyid",dest="policyid",help="policy id of the snapshot, if this is null, then use MANUAL_POLICY.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createSnapshot"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
