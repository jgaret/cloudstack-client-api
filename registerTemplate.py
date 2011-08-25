#! /usr/bin/python
"""
Registers an existing template into the Cloud.com cloud.
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

    parser = argparse.ArgumentParser(description="Registers an existing template into the Cloud.com cloud.")
 
    parser.add_argument("displaytext",help="the display text of the template. This is usually used for display purposes.")
    parser.add_argument("format",help="the format for the template. Possible values include QCOW2, RAW, and VHD.")
    parser.add_argument("hypervisor",help="the target hypervisor for the template")
    parser.add_argument("name",help="the name of the template")
    parser.add_argument("ostypeid",help="the ID of the OS Type that best represents the OS of this template.")
    parser.add_argument("url",help="the URL of where the template is hosted. Possible URL include http:// and https://")
    parser.add_argument("zoneid",help="the ID of the zone the template is to be hosted on")
    parser.add_argument("--account",dest="account",help="an optional accountName. Must be used with domainId.")
    parser.add_argument("--bits",dest="bits",help="32 or 64 bits support. 64 by default")
    parser.add_argument("--checksum",dest="checksum",help="the MD5 checksum value of this template")
    parser.add_argument("--domainid",dest="domainid",help="an optional domainId. If the account parameter is used, domainId must also be used.")
    parser.add_argument("--isextractable",dest="isextractable",help="true if the template or its derivatives are extractable; default is true")
    parser.add_argument("--isfeatured",dest="isfeatured",help="true if this template is a featured template, false otherwise")
    parser.add_argument("--ispublic",dest="ispublic",help="true if the template is available to all accounts; default is true")
    parser.add_argument("--passwordenabled",dest="passwordenabled",help="true if the template supports the password reset feature; default is false")
    parser.add_argument("--requireshvm",dest="requireshvm",help="true if this template requires HVM")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "registerTemplate"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
