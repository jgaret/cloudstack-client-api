#! /usr/bin/python
"""
Updates iso permissions
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

    parser = argparse.ArgumentParser(description="Updates iso permissions")
 
    parser.add_argument("id",help="the template ID")
    parser.add_argument("--accounts",dest="accounts",help="a comma delimited list of accounts. If specified, "op" parameter has to be passed in.")
    parser.add_argument("--isextractable",dest="isextractable",help="true if the template/iso is extractable, false other wise. Can be set only by root admin")
    parser.add_argument("--isfeatured",dest="isfeatured",help="true for featured template/iso, false otherwise")
    parser.add_argument("--ispublic",dest="ispublic",help="true for public template/iso, false for private templates/isos")
    parser.add_argument("--op",dest="op",help="permission operator (add, remove, reset)")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateIsoPermissions"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
