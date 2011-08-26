#! /usr/bin/python
"""
Creates a service offering.
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

    parser = argparse.ArgumentParser(description="Creates a service offering.")
 
    parser.add_argument("cpunumber",help="the CPU number of the service offering")
    parser.add_argument("cpuspeed",help="the CPU speed of the service offering in MHz.")
    parser.add_argument("displaytext",help="the display text of the service offering")
    parser.add_argument("memory",help="the total memory of the service offering in MB")
    parser.add_argument("name",help="the name of the service offering")
    parser.add_argument("--domainid",dest="domainid",help="the ID of the containing domain, null for public offerings")
    parser.add_argument("--hosttags",dest="hosttags",help="the host tag for this service offering.")
    parser.add_argument("--issystem",dest="issystem",help="is this a system vm offering")
    parser.add_argument("--limitcpuuse",dest="limitcpuuse",help="restrict the CPU usage to committed service offering")
    parser.add_argument("--offerha",dest="offerha",help="the HA for the service offering")
    parser.add_argument("--storagetype",dest="storagetype",help="the storage type of the service offering. Values are local and shared.")
    parser.add_argument("--systemvmtype",dest="systemvmtype",help="the system VM type. Possible types are "consoleproxy" and "secondarystoragevm".")
    parser.add_argument("--tags",dest="tags",help="the tags for this service offering.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createServiceOffering"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
