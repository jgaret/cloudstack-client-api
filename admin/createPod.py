#! /usr/bin/python
"""
Creates a new Pod.
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

    parser = argparse.ArgumentParser(description="Creates a new Pod.")
 
    parser.add_argument("gateway",help="the gateway for the Pod")
    parser.add_argument("name",help="the name of the Pod")
    parser.add_argument("netmask",help="the netmask for the Pod")
    parser.add_argument("startip",help="the starting IP address for the Pod")
    parser.add_argument("zoneid",help="the Zone ID in which the Pod will be created")
    parser.add_argument("--allocationstate",dest="allocationstate",help="Allocation state of this Pod for allocation of new resources")
    parser.add_argument("--endip",dest="endip",help="the ending IP address for the Pod")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createPod"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
