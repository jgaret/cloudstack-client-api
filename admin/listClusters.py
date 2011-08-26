#! /usr/bin/python
"""
Lists clusters.
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

    parser = argparse.ArgumentParser(description="Lists clusters.")
 
    parser.add_argument("--allocationstate",dest="allocationstate",help="lists clusters by allocation state")
    parser.add_argument("--clustertype",dest="clustertype",help="lists clusters by cluster type")
    parser.add_argument("--hypervisor",dest="hypervisor",help="lists clusters by hypervisor type")
    parser.add_argument("--id",dest="id",help="lists clusters by the cluster ID")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="lists clusters by the cluster name")
    parser.add_argument("--podid",dest="podid",help="lists clusters by Pod ID")
    parser.add_argument("--zoneid",dest="zoneid",help="lists clusters by Zone ID")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listClusters"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
