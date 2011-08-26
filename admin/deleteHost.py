#! /usr/bin/python
"""
Deletes a host.
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

    parser = argparse.ArgumentParser(description="Deletes a host.")
 
    parser.add_argument("id",help="the host ID")
    parser.add_argument("--forced",dest="forced",help="Force delete the host. All HA enabled vms running on the host will be put to HA; HA disabled ones will be stopped")
    parser.add_argument("--forcedestroylocalstorage",dest="forcedestroylocalstorage",help="Force destroy local storage on this host. All VMs created on this local storage will be destroyed")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "deleteHost"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
