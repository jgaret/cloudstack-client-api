#! /usr/bin/python
"""
Lists all port forwarding rules for an IP address.
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

    parser = argparse.ArgumentParser(description="Lists all port forwarding rules for an IP address.")
 
    parser.add_argument("--account",dest="account",help="account. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID. If used with the account parameter, lists port forwarding rules for the specified account in this domain.")
    parser.add_argument("--id",dest="id",help="Lists rule with the specified ID.")
    parser.add_argument("--ipaddressid",dest="ipaddressid",help="the id of IP address of the port forwarding services")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listPortForwardingRules"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
