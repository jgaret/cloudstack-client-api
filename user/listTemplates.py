#! /usr/bin/python
"""
List all public, private, and privileged templates.
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

    parser = argparse.ArgumentParser(description="List all public, private, and privileged templates.")
 
    parser.add_argument("templatefilter",help="possible values are 'featured', 'self', 'self-executable', 'executable', and 'community'.* featured-templates that are featured and are public* self-templates that have been registered/created by the owner* selfexecutable-templates that have been registered/created by the owner that can be used to deploy a new VM* executable-all templates that can be used to deploy a new VM* community-templates that are public.")
    parser.add_argument("--account",dest="account",help="list template by account. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="list all templates in specified domain. If used with the account parameter, lists all templates for an account in the specified domain.")
    parser.add_argument("--hypervisor",dest="hypervisor",help="the hypervisor for which to restrict the search")
    parser.add_argument("--id",dest="id",help="the template ID")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="the template name")
    parser.add_argument("--zoneid",dest="zoneid",help="list templates by zoneId")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listTemplates"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
