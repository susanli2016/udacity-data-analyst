import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import codecs
import pprint

OSMFILE = 'boston_massachusetts.osm'
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# Do not need to be cleaned
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Road", 
            "Parkway", "Plaza", "Broadway", "Circle", "Driveway", "Highway", "Park", "Lane"]

# The changes needed to fix the unexpected street types to the appropriate
# ones in the expected list
mapping = {"St": "Street",
           "st": "Street",
           "Street.": "Street", 
           "street": "Street",
           "St.": "Street",
           "St,": "Street", 
           "ST": "Street",
           "Rd.": "Road", 
           "Ave": "Avenue", 
           "Ave.": "Avenue",
           "Pkwy": "Parkway", 
           "rd.": "Road", 
           "Ct": "Court",  
           "Dr": "Drive", 
           "Rd": "Road", 
           "Hwy": "Highway", 
           "Sq.": "Square"}

def audit_street_type(street_types, street_name):
    """
       collects the last words in the "street_name" strings, if they are not
       within the expected list, then stores them
    """
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            
def is_street_name(elem):
    """
        looks for tags that specify street names(k="addr:street")
    """
    return (elem.attrib['k'] == "addr:street")

def audit(osmfile):
    """
        returns me a dictionary that match the above function conditions
    """
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

def update_name(name, mapping):
    """takes an old name to mapping dictionary, and update to a new one"""
    m = street_type_re.search(name)
    if m not in expected:
        if m.group() in mapping.keys():
            name = re.sub(m.group(), mapping[m.group()], name)
    
    return name
    
st_types = audit(OSMFILE)
pprint.pprint(st_types)
print(update_name("Boston St", mapping))
