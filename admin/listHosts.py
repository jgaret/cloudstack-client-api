#! /usr/bin/python
"""
Lists hosts.
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

    parser = argparse.ArgumentParser(description="Lists hosts.")
 
    parser.add_argument("--allocationstate",dest="allocationstate",help="list hosts by allocation state")
    parser.add_argument("--clusterid",dest="clusterid",help="lists hosts existing in particular cluster")
    parser.add_argument("--id",dest="id",help="the id of the host")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="the name of the host")
    parser.add_argument("--podid",dest="podid",help="the Pod ID for the host")
    parser.add_argument("--state",dest="state",help="the state of the host")
    parser.add_argument("--type",dest="type",help="the host type")
    parser.add_argument("--virtualmachineid",dest="virtualmachineid",help="lists hosts in the same cluster as this VM and flag hosts with enough CPU/RAm to host this VM")
    parser.add_argument("--zoneid",dest="zoneid",help="the Zone ID for the host")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listHosts"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
