#! /usr/bin/python
"""
Updates a network
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

    parser = argparse.ArgumentParser(description="Updates a network")
 
    parser.add_argument("id",help="the ID of the network")
    parser.add_argument("--displaytext",dest="displaytext",help="the new display text for the network")
    parser.add_argument("--name",dest="name",help="the new name for the network")
    parser.add_argument("--networkdomain",dest="networkdomain",help="network domain")
    parser.add_argument("--tags",dest="tags",help="tags for the network")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateNetwork"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
