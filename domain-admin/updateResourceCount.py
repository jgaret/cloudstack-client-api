#! /usr/bin/python
"""
Recalculate and update resource count for an account or domain.
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

    parser = argparse.ArgumentParser(description="Recalculate and update resource count for an account or domain.")
 
    parser.add_argument("domainid",help="If account parameter specified then updates resource counts for a specified account in this domain else update resource counts for all accounts &amp; child domains in specified domain.")
    parser.add_argument("--account",dest="account",help="Update resource count for a specified account. Must be used with the domainId parameter.")
    parser.add_argument("--resourcetype",dest="resourcetype",help="Type of resource to update. If specifies valid values are 0, 1, 2, 3, and 4. If not specified will update all resource counts0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot. Number of snapshots a user can create.4 - Template. Number of templates that a user can register/create.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateResourceCount"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
