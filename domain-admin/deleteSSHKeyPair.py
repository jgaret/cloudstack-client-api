#! /usr/bin/python
"""
Deletes a keypair by name
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

    parser = argparse.ArgumentParser(description="Deletes a keypair by name")
 
    parser.add_argument("name",help="Name of the keypair")
    parser.add_argument("--account",dest="account",help="the account associated with the keypair. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID associated with the keypair")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "deleteSSHKeyPair"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
