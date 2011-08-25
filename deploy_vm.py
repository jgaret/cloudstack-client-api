#! /usr/bin/python

import handleurl.handleurl as hu
import argparse
import pprint
import urllib2
from xml.dom import minidom

if __name__ == "__main__":
    apikey=hu.getenv_apikey()
    secretkey=hu.getenv_secretkey()
    url=hu.getenv_url()

    parser = argparse.ArgumentParser(description="Deploy a new VM - wrapper to deployVirtualMachine")
    parser.add_argument("serviceofferingid",help="Service offering Id")
    parser.add_argument("templateid",help="Template Id")
    parser.add_argument("zoneid",help="Zone Id")
    parser.add_argument("-a", "--account", dest="account", help="an optional account for the virtual machine. Must be used with domainId.")
    parser.add_argument("--diskofferingid", dest="diskofferingid", help="the ID of the disk offering for the virtual machine. If the template is of ISO format, the diskOfferingId is for the root disk volume. Otherwise this parameter is used to indicate the offering for the data disk volume. If the templateId parameter passed is from a Template object, the diskOfferingId refers to a DATA Disk Volume created. If the templateId parameter passed is from an ISO object, the diskOfferingId refers to a ROOT Disk Volume created.")
    parser.add_argument("-n", "--displayname", dest="displayname", help="an optional user generated name for the virtual machine")
    parser.add_argument("--domainid", dest="domainid", help="an optional domainId for the virtual machine. If the account parameter is used, domainId must also be used.")
    parser.add_argument("-g", "--group", dest="group", help="an optional group for the virtual machine")
    parser.add_argument("--hostid", dest="hostid", help="destination Host ID to deploy the VM to - parameter available for root admin only")
    parser.add_argument("--hypervisor", dest="hypervisor", help="the hypervisor on which to deploy the virtual machine")
    parser.add_argument("-k", "--keypair", dest="keypair", help="name of the ssh key pair used to login to the virtual machine")
    parser.add_argument("--name", dest="name", help="host name for the virtual machine")
    parser.add_argument("--networkids", dest="networkids", help="list of network ids used by virtual machine")
    parser.add_argument("--securitygroupids", dest="securitygroupids", help="comma separated list of security groups id that going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupnames parameter")
    parser.add_argument("--securitygroupnames", dest="securitygroupnames", help="comma separated list of security groups names that going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupids parameter")
    parser.add_argument("-s","--size", dest="size", help="the arbitrary size for the DATADISK volume. Mutually exclusive with diskOfferingId")


    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "deployVirtualMachine"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    print "URL = " + formatted_url 

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e


