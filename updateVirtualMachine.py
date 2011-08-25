#! /usr/bin/python
"""
Updates parameters of a virtual machine.
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

    parser = argparse.ArgumentParser(description="Updates parameters of a virtual machine.")
 
    parser.add_argument("id",help="The ID of the virtual machine")
    parser.add_argument("--displayname",dest="displayname",help="user generated name")
    parser.add_argument("--group",dest="group",help="group of the virtual machine")
    parser.add_argument("--haenable",dest="haenable",help="true if high-availability is enabled for the virtual machine, false otherwise")
    parser.add_argument("--ostypeid",dest="ostypeid",help="the ID of the OS type that best represents this VM.")
    parser.add_argument("--userdata",dest="userdata",help="an optional binary data that can be sent to the virtual machine upon a successful deployment. This binary data must be base64 encoded before adding it to the request. Currently only HTTP GET is supported. Using HTTP GET (via querystring), you can send up to 2KB of data after base64 encoding.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateVirtualMachine"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
