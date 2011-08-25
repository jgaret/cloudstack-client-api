#! /usr/bin/python
""" Common methods used to generate urls for use with cloudstack api
Main focus has to be on format_url()
"""
import hmac, hashlib
import base64
import argparse
import os, sys
import urllib2
from xml.dom import minidom

def url_encode(cmd, apikey, secretkey):
    """ Encode URL and return signature """ 
    cmd = cmd+"&apikey="+apikey

    # Sort command
    cmd = cmd.split("&")
    cmd.sort(key=lambda x: x[0])
    cmd = "&".join(cmd)

    # remove '+' signs
    cmd = cmd.lower().replace('+','%20')

    # generate the digest
    digest = base64.b64encode(hmac.new(secretkey, cmd, hashlib.sha1).digest())

    #transform the digest in an url compliant way
    digest = digest.replace('+','%2B')
    digest = digest.replace('=','%3D')
    
    return digest


def command_encode(command, option_list=[]):
    """ Correctly encode command and do sanity checks """
    if len(option_list) > 0:
        return "command="+command+'&'+'&'.join(option_list)
    else:
        return "command="+command

def format_url(command, url, apikey, secretkey, option_list=[]):
    """ Method used to format an url the cloudstack way """
    encoded_command = command_encode(command, option_list=option_list)
    print encoded_command
    digest = url_encode(encoded_command, apikey, secretkey)

    return url + "api?apikey=" + apikey + "&" + encoded_command + "&signature=" + digest


def get_env_api_key():
    """ Get the api key from environment variables. 
    These variables can be 'CS_API_KEY' or 'EC2_ACCESS_KEY'
    """
    # Get API Key from env
    if os.getenv("CS_API_KEY") is None:
        if os.getenv("EC2_ACCESS_KEY") is None:
            return False
        else:
            return os.getenv("EC2_ACCESS_KEY")
    else:
        return os.getenv("CS_API_KEY")


def get_env_secret_key():
    """ Get the secret key from environment variables. 
    These variables can be 'CS_SECRET_KEY' or 'EC2_SECRET_KEY'
    """
    # Get secret Key from env
    if os.getenv("CS_SECRET_KEY") is None:
        if os.getenv("EC2_SECRET_KEY") is None:
            return False
        else:
            return os.getenv("EC2_SECRET_KEY")
    else:
        return os.getenv("CS_SECRET_KEY")
    
def get_env_url():
    """ Get the url from environment variables.
    Theses variables can be 'CS_URL' or 'EC2_URL'
    """
    # Get URL from env
    if os.getenv("CS_URL") is None:
        if os.getenv("EC2_URL") is None:
            return False
        else:
            return os.getenv("EC2_URL")
    else:
        return os.getenv("CS_URL")
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="generate url from Cloudstack API")
    parser.add_argument ('command', help="The API command to use")
    parser.add_argument ('-o', '--options', dest = "options", nargs = "*", 
        help="Options for the command used")
    parser.add_argument ('-a', '--apikey', dest = "apikey", 
        help = "User's API Key")
    parser.add_argument ('-s', '--secretkey', dest = "secretkey", 
        help="User's secret key")
    parser.add_argument ('-u', '--url', dest = "url", 
        help='url of the cloudstack server')
    parser.add_argument ('-c', '--call', dest = "call", action = 'store_true', 
        help='call the url from this script')
    parser.add_argument ('-p', '--print', dest = "toPrint",
        action = 'store_true', help='print the url')

    args = parser.parse_args()

    if args.options is None:
        options = []
    else:
        options = args.options

    if args.apikey is None:
        akey = get_env_api_key()
        if not akey:
            sys.exit("APIKey not defined (neither as argument nor as env")
    else:
        akey = args.apikey

    if args.secretkey is None:
        skey = get_env_secret_key()
        if not skey:
            sys.exit("SecretKey not defined (neither as argument nor as env")
    else:
        skey = args.skey

    if args.url is None:
        csurl = get_env_url()
        if not csurl:
            sys.exit("URL not defined (neither as arguement nor as env")
    else:
        csurl = args.url

    formatted_url = format_url(command=args.command, option_list=options,
        url=csurl, apikey=akey, secretkey=skey)

    if args.toPrint:
        print "URL = " + formatted_url+"\n"

    if args.call:
        try: 
            response = urllib2.urlopen(formatted_url).read()
            xmldoc = minidom.parseString(response)
            print xmldoc.toprettyxml()
        except Exception, e:
            print 'Error !', e

