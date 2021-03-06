#! /usr/bin/python
"""
List system virtual machines.
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

    parser = argparse.ArgumentParser(description="List system virtual machines.")
 
    parser.add_argument("--hostid",dest="hostid",help="the host ID of the system VM")
    parser.add_argument("--id",dest="id",help="the ID of the system VM")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="the name of the system VM")
    parser.add_argument("--podid",dest="podid",help="the Pod ID of the system VM")
    parser.add_argument("--state",dest="state",help="the state of the system VM")
    parser.add_argument("--systemvmtype",dest="systemvmtype",help="the system VM type. Possible types are "consoleproxy" and "secondarystoragevm".")
    parser.add_argument("--zoneid",dest="zoneid",help="the Zone ID of the system VM")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listSystemVms"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
