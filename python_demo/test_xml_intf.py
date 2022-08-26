import json
import sys
import re
from datetime import date
import jsonpath
from bs4 import BeautifulSoup as Soup
import xmltodict
from Test_Modules import implement
from dicttoxml import dicttoxml

obj_Xlm_Intf = implement.Fs_Intf_Xml()


def get_endpoint_json_intf():
    endpoint_json_receiver = obj_Xlm_Intf.get_json_from_file("Config", "json_receiver_endpoint.json")
    create_xml_intf_endpoint = json.loads(endpoint_json_receiver)["xml_intf"]
    print(create_xml_intf_endpoint)
    return create_xml_intf_endpoint


# get_endpoint_json_intf()

def test_Xml_Intf_001():
    input_json_dict = obj_Xlm_Intf.get_json_from_file("Intf_Payload", "xml_intf_req.xml")
    request_xml = input_json_dict
    print(f"The custom header returned is:{obj_Xlm_Intf.get_headers_valid_token()}")
    response = obj_Xlm_Intf.post_call(get_endpoint_json_intf(), request_xml, obj_Xlm_Intf.get_headers_valid_token())
    # soup = Soup(response, 'xml')
    print("##url##", get_endpoint_json_intf())
    # print("##TOKEN##", get_headers_valid_token())
    print("#request#", request_xml)
    # print("#######", response.content)
    xml_dict_data = xmltodict.parse(response.content)
    print("#######", xml_dict_data)
    # Parse Response to Python Dict format
    assert int(xml_dict_data['mgage-response']['status']['code']) == 200
    assert xml_dict_data['mgage-response']['status']['desc'] == 'Request accepted'
    assert xml_dict_data['mgage-response']['ackid'] != ''

    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match_date = pattern.findall(xml_dict_data['mgage-response']['time'])
    assert match_date[0] == str(date.today())

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
    # validate_field_mandatory_error(response_json, "ruleName")

def test_xml_intf_api_with_valid_cust_ref_49():
    input_json_dict = obj_Xlm_Intf.get_json_from_file("Intf_Payload", "xml_intf_req.xml")
    request_xml = input_json_dict
    request_xml = request_xml.replace(">cust_ref<", ">cust_ref<")
    print(f"The custom header returned is:{obj_Xlm_Intf.get_headers_valid_token()}")
    response = obj_Xlm_Intf.post_call(get_endpoint_json_intf(), request_xml, obj_Xlm_Intf.get_headers_valid_token())
    # soup = Soup(response, 'xml')
    print("##url##", get_endpoint_json_intf())
    # print("##TOKEN##", get_headers_valid_token())
    print("#request#", request_xml)
    # print("#######", response.content)
    xml_dict_data = xmltodict.parse(response.content)
    print("#######", xml_dict_data)
    # Parse Response to Python Dict format
    assert int(xml_dict_data['mgage-response']['status']['code']) == 200
    assert xml_dict_data['mgage-response']['status']['desc'] == 'Request accepted'
    assert xml_dict_data['mgage-response']['ackid'] != ''

    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match_date = pattern.findall(xml_dict_data['mgage-response']['time'])
    assert match_date[0] == str(date.today())

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
    # validate_field_mandatory_error(response_json, "ruleName")


def test_xml_intf_api_with_empty_cust_ref_50():
    input_json_dict = obj_Xlm_Intf.get_json_from_file("Intf_Payload", "xml_intf_req.xml")
    request_xml = input_json_dict
    request_xml = request_xml.replace(">cust_ref<", "><")
    print(f"The custom header returned is:{obj_Xlm_Intf.get_headers_valid_token()}")
    response = obj_Xlm_Intf.post_call(get_endpoint_json_intf(), request_xml, obj_Xlm_Intf.get_headers_valid_token())
    # soup = Soup(response, 'xml')
    print("##url##", get_endpoint_json_intf())
    # print("##TOKEN##", get_headers_valid_token())
    print("#request#", request_xml)
    # print("#######", response.content)
    xml_dict_data = xmltodict.parse(response.content)
    print("#######", xml_dict_data)
    # Parse Response to Python Dict format
    assert int(xml_dict_data['mgage-response']['status']['code']) == 200
    assert xml_dict_data['mgage-response']['status']['desc'] == 'Request accepted'
    assert xml_dict_data['mgage-response']['ackid'] != ''

    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match_date = pattern.findall(xml_dict_data['mgage-response']['time'])
    assert match_date[0] == str(date.today())

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
    # validate_field_mandatory_error(response_json, "ruleName")


def test_xml_intf_api_with_valid_country_code_51():
    input_json_dict = obj_Xlm_Intf.get_json_from_file("Intf_Payload", "xml_intf_req.xml")
    request_xml = input_json_dict
    request_xml = request_xml.replace(">91<", ">91<")
    print(f"The custom header returned is:{obj_Xlm_Intf.get_headers_valid_token()}")
    response = obj_Xlm_Intf.post_call(get_endpoint_json_intf(), request_xml, obj_Xlm_Intf.get_headers_valid_token())
    # soup = Soup(response, 'xml')
    print("##url##", get_endpoint_json_intf())
    # print("##TOKEN##", get_headers_valid_token())
    print("#request#", request_xml)
    # print("#######", response.content)
    xml_dict_data = xmltodict.parse(response.content)
    print("#######", xml_dict_data)
    # Parse Response to Python Dict format
    assert int(xml_dict_data['mgage-response']['status']['code']) == 200
    assert xml_dict_data['mgage-response']['status']['desc'] == 'Request accepted'
    assert xml_dict_data['mgage-response']['ackid'] != ''

    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match_date = pattern.findall(xml_dict_data['mgage-response']['time'])
    assert match_date[0] == str(date.today())

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
    # validate_field_mandatory_error(response_json, "ruleName")


def test_xml_intf_api_with_invalid_country_code_52():
    input_json_dict = obj_Xlm_Intf.get_json_from_file("Intf_Payload", "xml_intf_req.xml")
    request_xml = input_json_dict
    request_xml = request_xml.replace(">91<", ">abc<")
    print(f"The custom header returned is:{obj_Xlm_Intf.get_headers_valid_token()}")
    response = obj_Xlm_Intf.post_call(get_endpoint_json_intf(), request_xml, obj_Xlm_Intf.get_headers_valid_token())
    # soup = Soup(response, 'xml')
    print("##url##", get_endpoint_json_intf())
    # print("##TOKEN##", get_headers_valid_token())
    print("#request#", request_xml)
    # print("#######", response.content)
    xml_dict_data = xmltodict.parse(response.content)
    print("#######", xml_dict_data)
    # Parse Response to Python Dict format
    assert int(xml_dict_data['mgage-response']['status']['code']) == 200
    assert xml_dict_data['mgage-response']['status']['desc'] == 'Request accepted'
    assert xml_dict_data['mgage-response']['ackid'] != ''

    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match_date = pattern.findall(xml_dict_data['mgage-response']['time'])
    assert match_date[0] == str(date.today())

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
    # validate_field_mandatory_error(response_json, "ruleName")


def test_xml_intf_api_with_valid_version_53():
    input_json_dict = obj_Xlm_Intf.get_json_from_file("Intf_Payload", "xml_intf_req.xml")
    request_xml = input_json_dict
    request_xml = request_xml.replace('ver="1.0"', 'ver="1.0"')
    print(f"The custom header returned is:{obj_Xlm_Intf.get_headers_valid_token()}")
    response = obj_Xlm_Intf.post_call(get_endpoint_json_intf(), request_xml, obj_Xlm_Intf.get_headers_valid_token())
    # soup = Soup(response, 'xml')
    print("##url##", get_endpoint_json_intf())
    # print("##TOKEN##", get_headers_valid_token())
    print("#request#", request_xml)
    # print("#######", response.content)
    xml_dict_data = xmltodict.parse(response.content)
    print("#######", xml_dict_data)
    # Parse Response to Python Dict format
    assert int(xml_dict_data['mgage-response']['status']['code']) == 200
    assert xml_dict_data['mgage-response']['status']['desc'] == 'Request accepted'
    assert xml_dict_data['mgage-response']['ackid'] != ''

    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match_date = pattern.findall(xml_dict_data['mgage-response']['time'])
    assert match_date[0] == str(date.today())

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
    # validate_field_mandatory_error(response_json, "ruleName")


def test_xml_intf_api_with_empty_version_54():
    input_json_dict = obj_Xlm_Intf.get_json_from_file("Intf_Payload", "xml_intf_req.xml")
    request_xml = input_json_dict
    request_xml = request_xml.replace('ver="1.0"', 'ver=""')
    print(f"The custom header returned is:{obj_Xlm_Intf.get_headers_valid_token()}")
    response = obj_Xlm_Intf.post_call(get_endpoint_json_intf(), request_xml, obj_Xlm_Intf.get_headers_valid_token())
    # soup = Soup(response, 'xml')
    print("##url##", get_endpoint_json_intf())
    # print("##TOKEN##", get_headers_valid_token())
    print("#request#", request_xml)
    # print("#######", response.content)
    xml_dict_data = xmltodict.parse(response.content)
    print("#######", xml_dict_data)
    # Parse Response to Python Dict format
    assert int(xml_dict_data['mgage-response']['status']['code']) == 200
    assert xml_dict_data['mgage-response']['status']['desc'] == 'Request accepted'
    assert xml_dict_data['mgage-response']['ackid'] != ''

    assert int(xml_dict_data['mgage-response']['status']['code']) == '-101'
    # assert xml_dict_data['mgage-response']['status']['desc'] == 'Invalid API version ( Version field is missing )'
    # assert xml_dict_data['mgage-response']['ackid'] != 'N/A'

    pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    match_date = pattern.findall(xml_dict_data['mgage-response']['time'])
    assert match_date[0] == str(date.today())

    # Assert Mandatory Field level validation errors
    # validate_field_mandatory_error(response_json, "status")
    # validate_field_mandatory_error(response_json, "message")
    # validate_field_mandatory_error(response_json, "ruleName")

