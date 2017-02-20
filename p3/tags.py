import xml.etree.cElementTree as ET
import re
import pprint

# Tags that contain only lowercase letters and are valid
lower = re.compile(r'^([a-z]|_)*$')
# Valid tags with a colon in their names
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
# Tags with problematic characters
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys):
    """ check k value for each tag"""
    if element.tag == "tag":
        key = element.attrib['k']
        if re.search(lower, key) is not None:
            keys['lower']+=1
        elif re.search(lower_colon, key) is not None:
            keys['lower_colon']+=1
        elif re.search(problemchars, key) is not None:
            keys['problemchars'] +=1
        else:
            keys['other']+=1
        
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys
pprint.pprint(process_map('boston_massachusetts.osm'))
