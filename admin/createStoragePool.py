#! /usr/bin/python
"""
Creates a storage pool.
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

    parser = argparse.ArgumentParser(description="Creates a storage pool.")
 
    parser.add_argument("name",help="the name for the storage pool")
    parser.add_argument("url",help="the URL of the storage pool")
    parser.add_argument("zoneid",help="the Zone ID for the storage pool")
    parser.add_argument("--clusterid",dest="clusterid",help="the cluster ID for the storage pool")
    parser.add_argument("--details",dest="details",help="the details for the storage pool")
    parser.add_argument("--podid",dest="podid",help="the Pod ID for the storage pool")
    parser.add_argument("--tags",dest="tags",help="the tags for the storage pool")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createStoragePool"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
