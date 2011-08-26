#! /usr/bin/python
"""
List routers.
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

    parser = argparse.ArgumentParser(description="List routers.")
 
    parser.add_argument("--account",dest="account",help="the name of the account associated with the router. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID associated with the router. If used with the account parameter, lists all routers associated with an account in the specified domain.")
    parser.add_argument("--hostid",dest="hostid",help="the host ID of the router")
    parser.add_argument("--id",dest="id",help="the ID of the disk router")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="the name of the router")
    parser.add_argument("--networkid",dest="networkid",help="list by network id")
    parser.add_argument("--podid",dest="podid",help="the Pod ID of the router")
    parser.add_argument("--state",dest="state",help="the state of the router")
    parser.add_argument("--zoneid",dest="zoneid",help="the Zone ID of the router")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listRouters"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
