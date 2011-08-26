#! /usr/bin/python
"""
Lists all volumes.
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

    parser = argparse.ArgumentParser(description="Lists all volumes.")
 
    parser.add_argument("--account",dest="account",help="the account associated with the disk volume. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="Lists all disk volumes for the specified domain ID. If used with the account parameter, returns all disk volumes for an account in the specified domain ID.")
    parser.add_argument("--hostid",dest="hostid",help="list volumes on specified host")
    parser.add_argument("--id",dest="id",help="the ID of the disk volume")
    parser.add_argument("--isrecursive",dest="isrecursive",help="defaults to false, but if true, lists all volumes from the parent specified by the domain id till leaves.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="the name of the disk volume")
    parser.add_argument("--podid",dest="podid",help="the pod id the disk volume belongs to")
    parser.add_argument("--type",dest="type",help="the type of disk volume")
    parser.add_argument("--virtualmachineid",dest="virtualmachineid",help="the ID of the virtual machine")
    parser.add_argument("--zoneid",dest="zoneid",help="the ID of the availability zone")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listVolumes"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
