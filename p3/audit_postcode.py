import xml.etree.cElementTree as ET
import re
import pprint
from collections import defaultdict

osmfile = "boston_massachusetts.osm"


def is_postcode(elem):
    """check if elem is a postcode"""
    return (elem.attrib['k'] == "addr:postcode" or elem.attrib['k'] == "postal_code")

def audit_postcode(postcodes, postcode):
    """ Get a full list of entries about postcode """
    postcodes[postcode].add(postcode)
    return postcodes

def audit_post(osmfile):
    """ match above function conditions """
    osm_file=open(osmfile, 'r')
    postcodes = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_postcode(tag):
                    postcodes = audit_postcode(postcodes, tag.attrib["v"])
    osm_file.close()
    pprint.pprint(dict(postcodes))
audit_post(osmfile)


def update_postcode(postcode):
    """Clean postcode to a uniform format of 5 digit; Return updated postcode"""
    if re.findall(r'^\d{5}$', postcode): # 5 digits
        valid_postcode = postcode
        return valid_postcode
    elif re.findall(r'(^\d{5})-\d{4}$', postcode): # 9 digits
        valid_postcode = re.findall(r'(^\d{5})-\d{4}$', postcode)[0]
        return valid_postcode
    elif re.findall(r'MA\s*\d{5}', postcode): # with state code
        valid_postcode =re.findall(r'\d{5}', postcode)[0]  
        return valid_postcode  
    else:
        return None
