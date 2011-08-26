#! /usr/bin/python
"""
Adds configuration value
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

    parser = argparse.ArgumentParser(description="Adds configuration value")
 
    parser.add_argument("category",help="component's category")
    parser.add_argument("component",help="the component of the configuration")
    parser.add_argument("instance",help="the instance of the configuration")
    parser.add_argument("name",help="the name of the configuration")
    parser.add_argument("--description",dest="description",help="the description of the configuration")
    parser.add_argument("--value",dest="value",help="the value of the configuration")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createConfiguration"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
