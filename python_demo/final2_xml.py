
import xmltodict
from dicttoxml import dicttoxml

myxml = open('D:\\demo\\python_demo\\fs_intf_req.xml', 'r').read()
xml_file = xmltodict.parse(myxml)
print(xml_file)
# # xml_file["urlset"]["url"][0]["changefreq"]="shakya"
xml_file["request"]["messages"].update({"tiger":123})
# x.update({"tiger":123})
#
xml_file_new = xmltodict.unparse(xml_file)
print(xml_file_new)
