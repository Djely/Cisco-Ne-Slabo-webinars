from tokenize import group
import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()

ns = re.match('{.*}', root.tag).group(0)
editconf = root.find