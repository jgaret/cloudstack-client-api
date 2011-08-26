#! /usr/bin/python
"""
List the virtual machines owned by the account.
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

    parser = argparse.ArgumentParser(description="List the virtual machines owned by the account.")
 
    parser.add_argument("--account",dest="account",help="account. Must be used with the domainId parameter.")
    parser.add_argument("--domainid",dest="domainid",help="the domain ID. If used with the account parameter, lists virtual machines for the specified account in this domain.")
    parser.add_argument("--forvirtualnetwork",dest="forvirtualnetwork",help="list by network type; true if need to list vms using Virtual Network, false otherwise")
    parser.add_argument("--groupid",dest="groupid",help="the group ID")
    parser.add_argument("--hostid",dest="hostid",help="the host ID")
    parser.add_argument("--hypervisor",dest="hypervisor",help="the target hypervisor for the template")
    parser.add_argument("--id",dest="id",help="the ID of the virtual machine")
    parser.add_argument("--isrecursive",dest="isrecursive",help="Must be used with domainId parameter. Defaults to false, but if true, lists all vms from the parent specified by the domain id till leaves.")
    parser.add_argument("--keyword",dest="keyword",help="List by keyword")
    parser.add_argument("--name",dest="name",help="name of the virtual machine")
    parser.add_argument("--networkid",dest="networkid",help="list by network id")
    parser.add_argument("--podid",dest="podid",help="the pod ID")
    parser.add_argument("--state",dest="state",help="state of the virtual machine")
    parser.add_argument("--storageid",dest="storageid",help="the storage ID where vm's volumes belong to")
    parser.add_argument("--zoneid",dest="zoneid",help="the availability zone ID")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "listVirtualMachines"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
