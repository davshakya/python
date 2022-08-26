from xml.dom import xmlbuilder
import xml.etree.ElementTree as ET
tree = ET.parse('D:\\demo\\python_demo\\xml_intf_req.xml')
root = tree.getroot()
root[0][2].text="Mango"
print(root[0][2].text)
# read_xml=open("D:\\demo\\python_demo\\xml_intf_req.xml").read()
# print(read_xml)





