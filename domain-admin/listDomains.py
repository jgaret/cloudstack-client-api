#! /usr/bin/python
"""
Lists domains and provides detailed information for listed domains
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

    parser = argparse.ArgumentParser(description="Lists domains and provides detailed information for listed domains")
 
    parser.add_argument("--id",dest="id",help="List domain by domain ID.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--level",dest="level",help="List domains by domain level.")
    parser.add_argument("--name",dest="name",help="List domain by domain name.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listDomains"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
