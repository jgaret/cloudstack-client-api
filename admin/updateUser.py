#! /usr/bin/python
"""
Updates a user account
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

    parser = argparse.ArgumentParser(description="Updates a user account")
 
    parser.add_argument("id",help="User id")
    parser.add_argument("--email",dest="email",help="email")
    parser.add_argument("--firstname",dest="firstname",help="first name")
    parser.add_argument("--lastname",dest="lastname",help="last name")
    parser.add_argument("--password",dest="password",help="Hashed password (default is MD5). If you wish to use any other hasing algorithm, you would need to write a custom authentication adapter")
    parser.add_argument("--timezone",dest="timezone",help="Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format.")
    parser.add_argument("--userapikey",dest="userapikey",help="The API key for the user. Must be specified with userSecretKey")
    parser.add_argument("--username",dest="username",help="Unique username")
    parser.add_argument("--usersecretkey",dest="usersecretkey",help="The secret key for the user. Must be specified with userApiKey")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateUser"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
