import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
    """ The top tags and how many of each"""
    tags ={}
    for event, element in ET.iterparse(filename):
        tag= element.tag
        if tag not in tags.keys():
            tags[tag] =1
        else:
            tags[tag] += 1
    return tags
pprint.pprint(count_tags('boston_massachusetts.osm'))
