#! /usr/bin/python
"""
Update password of a host/pool on management server.
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

    parser = argparse.ArgumentParser(description="Update password of a host/pool on management server.")
 
    parser.add_argument("password",help="the password for the host/cluster")
    parser.add_argument("username",help="the username for the host/cluster")
    parser.add_argument("--clusterid",dest="clusterid",help="the cluster ID for the host")
    parser.add_argument("--hostid",dest="hostid",help="the host ID")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateHostPassword"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
