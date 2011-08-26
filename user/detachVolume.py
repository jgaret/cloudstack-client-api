#! /usr/bin/python
"""
Detaches a disk volume from a virtual machine.
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

    parser = argparse.ArgumentParser(description="Detaches a disk volume from a virtual machine.")
 
    parser.add_argument("--deviceid",dest="deviceid",help="the device ID on the virtual machine where volume is detached from")
    parser.add_argument("--id",dest="id",help="the ID of the disk volume")
    parser.add_argument("--virtualmachineid",dest="virtualmachineid",help="the ID of the virtual machine where the volume is detached from")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "detachVolume"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
