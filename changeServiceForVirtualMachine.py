#! /usr/bin/python
"""
Changes the service offering for a virtual machine. The virtual machine must be in a "Stopped" state for this command to take effect.
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

    parser = argparse.ArgumentParser(description="Changes the service offering for a virtual machine. The virtual machine must be in a "Stopped" state for this command to take effect.")
 
    parser.add_argument("id",help="The ID of the virtual machine")
    parser.add_argument("serviceofferingid",help="the service offering ID to apply to the virtual machine")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "changeServiceForVirtualMachine"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
