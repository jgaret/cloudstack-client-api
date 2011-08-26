#! /usr/bin/python
"""
Adds a new cluster
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

    parser = argparse.ArgumentParser(description="Adds a new cluster")
 
    parser.add_argument("clustername",help="the cluster name")
    parser.add_argument("clustertype",help="hypervisor type of the cluster")
    parser.add_argument("hypervisor",help="hypervisor type of the cluster")
    parser.add_argument("zoneid",help="the Zone ID for the cluster")
    parser.add_argument("--allocationstate",dest="allocationstate",help="Allocation state of this cluster for allocation of new resources")
    parser.add_argument("--password",dest="password",help="the password for the host")
    parser.add_argument("--podid",dest="podid",help="the Pod ID for the host")
    parser.add_argument("--url",dest="url",help="the URL")
    parser.add_argument("--username",dest="username",help="the username for the cluster")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "addCluster"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
