#! /usr/bin/python
"""
Create a new keypair and returns the private key
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

    parser = argparse.ArgumentParser(description="Create a new keypair and returns the private key")
 
    parser.add_argument("name",help="Name of the keypair")
    parser.add_argument("--account",dest="account",help="an optional account for the ssh key. Must be used with domainId.")
    parser.add_argument("--domainid",dest="domainid",help="an optional domainId for the ssh key. If the account parameter is used, domainId must also be used.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createSSHKeyPair"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
