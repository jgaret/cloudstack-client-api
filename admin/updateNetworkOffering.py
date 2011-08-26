#! /usr/bin/python
"""
Updates a network offering.
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

    parser = argparse.ArgumentParser(description="Updates a network offering.")
 
    parser.add_argument("--availability",dest="availability",help="the availability of network offering. Default value is Required for Guest Virtual network offering; Optional for Guest Direct network offering")
    parser.add_argument("--displaytext",dest="displaytext",help="the display text of the network offering")
    parser.add_argument("--id",dest="id",help="the id of the network offering")
    parser.add_argument("--name",dest="name",help="the name of the network offering")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateNetworkOffering"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
