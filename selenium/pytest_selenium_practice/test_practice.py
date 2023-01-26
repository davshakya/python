import time

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import validators


@pytest.mark.usefixtures("setup")
class TestLogin:
    # def test_selenium(self):
    #     # driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
    #     driver.find_element_by_id("name").send_keys("Devendra")
    #     print(driver.title)
    #     print(driver.current_url)

    def test_111(self):
        a = 2
        b = 2
        assert a == b


@pytest.mark.usefixtures("setup")
class TestParam:
    @pytest.mark.parametrize("count", [123, 345])
    def test_prm(self, count):
        print(count)
