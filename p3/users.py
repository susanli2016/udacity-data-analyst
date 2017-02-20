import xml.etree.cElementTree as ET
import pprint
import re


def get_user(element):
    """ Return a set if unique user IDs """
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib.keys():
            users.add(element.attrib['uid'])
        
    return users
pprint.pprint(process_map('boston_massachusetts.osm'))
