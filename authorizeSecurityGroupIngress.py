#! /usr/bin/python
"""
Authorizes a particular ingress rule for this security group
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

    parser = argparse.ArgumentParser(description="Authorizes a particular ingress rule for this security group")
 
    parser.add_argument("--account",dest="account",help="an optional account for the virtual machine. Must be used with domainId.")
    parser.add_argument("--cidrlist",dest="cidrlist",help="the cidr list associated")
    parser.add_argument("--domainid",dest="domainid",help="an optional domainId for the security group. If the account parameter is used, domainId must also be used.")
    parser.add_argument("--endport",dest="endport",help="end port for this ingress rule")
    parser.add_argument("--icmpcode",dest="icmpcode",help="error code for this icmp message")
    parser.add_argument("--icmptype",dest="icmptype",help="type of the icmp message being sent")
    parser.add_argument("--protocol",dest="protocol",help="TCP is default. UDP is the other supported protocol")
    parser.add_argument("--securitygroupid",dest="securitygroupid",help="The ID of the security group. Mutually exclusive with securityGroupName parameter")
    parser.add_argument("--securitygroupname",dest="securitygroupname",help="The name of the security group. Mutually exclusive with securityGroupName parameter")
    parser.add_argument("--startport",dest="startport",help="start port for this ingress rule")
    parser.add_argument("--usersecuritygrouplist",dest="usersecuritygrouplist",help="user to security group mapping")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "authorizeSecurityGroupIngress"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
