#! /usr/bin/python
"""
Adds a new host.
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

    parser = argparse.ArgumentParser(description="Adds a new host.")
 
    parser.add_argument("hypervisor",help="hypervisor type of the host")
    parser.add_argument("password",help="the password for the host")
    parser.add_argument("url",help="the host URL")
    parser.add_argument("username",help="the username for the host")
    parser.add_argument("zoneid",help="the Zone ID for the host")
    parser.add_argument("--allocationstate",dest="allocationstate",help="Allocation state of this Host for allocation of new resources")
    parser.add_argument("--clusterid",dest="clusterid",help="the cluster ID for the host")
    parser.add_argument("--clustername",dest="clustername",help="the cluster name for the host")
    parser.add_argument("--cpunumber",dest="cpunumber",help="Only for hypervisor is BareMetal, number of CPU on host")
    parser.add_argument("--cpuspeed",dest="cpuspeed",help="Only for hypervisor is BareMetal, HZ per CPU of host")
    parser.add_argument("--hostmac",dest="hostmac",help="Only for hypervisor is BareMetal, Mac of PXE nic")
    parser.add_argument("--hosttags",dest="hosttags",help="list of tags to be added to the host")
    parser.add_argument("--memory",dest="memory",help="Only for hypervisor is BareMetal, memory capacity of host(in MB)")
    parser.add_argument("--podid",dest="podid",help="the Pod ID for the host")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "addHost"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
