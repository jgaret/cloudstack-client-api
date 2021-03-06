#! /usr/bin/python
"""
Updates a Zone.
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

    parser = argparse.ArgumentParser(description="Updates a Zone.")
 
    parser.add_argument("id",help="the ID of the Zone")
    parser.add_argument("--allocationstate",dest="allocationstate",help="Allocation state of this cluster for allocation of new resources")
    parser.add_argument("--details",dest="details",help="the details for the Zone")
    parser.add_argument("--dhcpprovider",dest="dhcpprovider",help="the dhcp Provider for the Zone")
    parser.add_argument("--dns1",dest="dns1",help="the first DNS for the Zone")
    parser.add_argument("--dns2",dest="dns2",help="the second DNS for the Zone")
    parser.add_argument("--guestcidraddress",dest="guestcidraddress",help="the guest CIDR address for the Zone")
    parser.add_argument("--internaldns1",dest="internaldns1",help="the first internal DNS for the Zone")
    parser.add_argument("--internaldns2",dest="internaldns2",help="the second internal DNS for the Zone")
    parser.add_argument("--ispublic",dest="ispublic",help="updates a private zone to public if set, but not vice-versa")
    parser.add_argument("--name",dest="name",help="the name of the Zone")
    parser.add_argument("--vlan",dest="vlan",help="the VLAN for the Zone")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "updateZone"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
