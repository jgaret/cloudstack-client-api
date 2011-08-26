#! /usr/bin/python
"""
Updates attributes of a template.
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

    parser = argparse.ArgumentParser(description="Updates attributes of a template.")
 
    parser.add_argument("id",help="the ID of the image file")
    parser.add_argument("--bootable",dest="bootable",help="true if image is bootable, false otherwise")
    parser.add_argument("--displaytext",dest="displaytext",help="the display text of the image")
    parser.add_argument("--format",dest="format",help="the format for the image")
    parser.add_argument("--name",dest="name",help="the name of the image file")
    parser.add_argument("--ostypeid",dest="ostypeid",help="the ID of the OS type that best represents the OS of this image.")
    parser.add_argument("--passwordenabled",dest="passwordenabled",help="true if the image supports the password reset feature; default is false")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateTemplate"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
