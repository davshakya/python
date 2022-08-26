import json
from xml.etree import ElementTree
import xmltodict
from dict2xml import dict2xml
myxml=open('D:\\demo\\python_demo\\xml_intf_req.xml', 'r').read()
print(myxml)
my_dict=xmltodict.parse(myxml)
print(my_dict)

xmlfile

# print(myxml)
# my_dict=xmltodict.parse(myxml)
# print(my_dict)
# my_dict["request"]["messages"]["send"]="devendra"   
# print(new_dict["request"]["messages"]["send"])
# dict_xml=dict2xml(my_dict)
# print(dict_xml)



