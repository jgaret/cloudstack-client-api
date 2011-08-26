#! /usr/bin/python
"""
Creates a snapshot policy for the account.
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

    parser = argparse.ArgumentParser(description="Creates a snapshot policy for the account.")
 
    parser.add_argument("intervaltype",help="valid values are HOURLY, DAILY, WEEKLY, and MONTHLY")
    parser.add_argument("maxsnaps",help="maximum number of snapshots to retain")
    parser.add_argument("schedule",help="time the snapshot is scheduled to be taken. Format is:* if HOURLY, MM* if DAILY, MM:HH* if WEEKLY, MM:HH:DD (1-7)* if MONTHLY, MM:HH:DD (1-28)")
    parser.add_argument("timezone",help="Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format.")
    parser.add_argument("volumeid",help="the ID of the disk volume")

    args = parser.parse_args()

    #Transform args to key=value list
    options = [ "%s=%s" % (key , value) for key, value in vars(args).items() if not value is None]

    command = "createSnapshotPolicy"

    formatted_url = hu.format_url(command=command, option_list=options,url=url, apikey=apikey, secretkey=secretkey)

    try:
        response = urllib2.urlopen(formatted_url).read()
        xmldoc = minidom.parseString(response)
        print xmldoc.toprettyxml()
    except Exception, e:
        print 'Error !', e
    
