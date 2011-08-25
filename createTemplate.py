#! /usr/bin/python
"""
Creates a template of a virtual machine. The virtual machine must be in a STOPPED state. A template created from this command is automatically designated as a private template visible to the account that created it.
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

    parser = argparse.ArgumentParser(description="Creates a template of a virtual machine. The virtual machine must be in a STOPPED state. A template created from this command is automatically designated as a private template visible to the account that created it.")
 
    parser.add_argument("displaytext",help="the display text of the template. This is usually used for display purposes.")
    parser.add_argument("name",help="the name of the template")
    parser.add_argument("ostypeid",help="the ID of the OS Type that best represents the OS of this template.")
    parser.add_argument("--bits",dest="bits",help="32 or 64 bit")
    parser.add_argument("--isfeatured",dest="isfeatured",help="true if this template is a featured template, false otherwise")
    parser.add_argument("--ispublic",dest="ispublic",help="true if this template is a public template, false otherwise")
    parser.add_argument("--passwordenabled",dest="passwordenabled",help="true if the template supports the password reset feature; default is false")
    parser.add_argument("--requireshvm",dest="requireshvm",help="true if the template requres HVM, false otherwise")
    parser.add_argument("--snapshotid",dest="snapshotid",help="the ID of the snapshot the template is being created from. Either this parameter, or volumeId has to be passed in")
    parser.add_argument("--volumeid",dest="volumeid",help="the ID of the disk volume the template is being created from. Either this parameter, or snapshotId has to be passed in")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createTemplate"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
