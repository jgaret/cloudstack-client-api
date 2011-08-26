#! /usr/bin/python
"""
Updates a Pod.
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

    parser = argparse.ArgumentParser(description="Updates a Pod.")
 
    parser.add_argument("id",help="the ID of the Pod")
    parser.add_argument("--allocationstate",dest="allocationstate",help="Allocation state of this cluster for allocation of new resources")
    parser.add_argument("--endip",dest="endip",help="the ending IP address for the Pod")
    parser.add_argument("--gateway",dest="gateway",help="the gateway for the Pod")
    parser.add_argument("--name",dest="name",help="the name of the Pod")
    parser.add_argument("--netmask",dest="netmask",help="the netmask of the Pod")
    parser.add_argument("--startip",dest="startip",help="the starting IP address for the Pod")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updatePod"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
