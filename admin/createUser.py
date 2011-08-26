#! /usr/bin/python
"""
Creates a user for an account that already exists
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

    parser = argparse.ArgumentParser(description="Creates a user for an account that already exists")
 
    parser.add_argument("account",help="Creates the user under the specified account. If no account is specified, the username will be used as the account name.")
    parser.add_argument("email",help="email")
    parser.add_argument("firstname",help="firstname")
    parser.add_argument("lastname",help="lastname")
    parser.add_argument("password",help="Hashed password (Default is MD5). If you wish to use any other hashing algorithm, you would need to write a custom authentication adapter See Docs section.")
    parser.add_argument("username",help="Unique username.")
    parser.add_argument("--domainid",dest="domainid",help="Creates the user under the specified domain. Has to be accompanied with the account parameter")
    parser.add_argument("--timezone",dest="timezone",help="Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format.")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createUser"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
