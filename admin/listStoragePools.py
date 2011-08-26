#! /usr/bin/python
"""
Lists storage pools.
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

    parser = argparse.ArgumentParser(description="Lists storage pools.")
 
    parser.add_argument("--clusterid",dest="clusterid",help="list storage pools belongig to the specific cluster")
    parser.add_argument("--id",dest="id",help="the ID of the storage pool")
    parser.add_argument("--ipaddress",dest="ipaddress",help="the IP address for the storage pool")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="the name of the storage pool")
    parser.add_argument("--path",dest="path",help="the storage pool path")
    parser.add_argument("--podid",dest="podid",help="the Pod ID for the storage pool")
    parser.add_argument("--zoneid",dest="zoneid",help="the Zone ID for the storage pool")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listStoragePools"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
