#! /usr/bin/python
"""
Lists all available ISO files.
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

    parser = argparse.ArgumentParser(description="Lists all available ISO files.")
 
    parser.add_argument("--account",dest="account",help="the account of the ISO file. Must be used with the domainId parameter.")
    parser.add_argument("--bootable",dest="bootable",help="true if the ISO is bootable, false otherwise")
    parser.add_argument("--domainid",dest="domainid",help="lists all available ISO files by ID of a domain. If used with the account parameter, lists all available ISO files for the account in the ID of a domain.")
    parser.add_argument("--hypervisor",dest="hypervisor",help="the hypervisor for which to restrict the search")
    parser.add_argument("--id",dest="id",help="list all isos by id")
    parser.add_argument("--isofilter",dest="isofilter",help="possible values are "featured", "self", "self-executable","executable", and "community". * featured-ISOs that are featured and are publicself-ISOs that have been registered/created by the owner. * selfexecutable-ISOs that have been registered/created by the owner that can be used to deploy a new VM. * executable-all ISOs that can be used to deploy a new VM * community-ISOs that are public.")
    parser.add_argument("--ispublic",dest="ispublic",help="true if the ISO is publicly available to all users, false otherwise.")
    parser.add_argument("--isready",dest="isready",help="true if this ISO is ready to be deployed")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="list all isos by name")
    parser.add_argument("--zoneid",dest="zoneid",help="the ID of the zone")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listIsos"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
