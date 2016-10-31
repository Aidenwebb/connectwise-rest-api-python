"""Tests for client module"""

import responses
import time

import connectwise
from connectwise import client as _client
import test as _test
import requests

class ClientTest(_test.TestCase):

    def test_no_api_key(self):
        with self.assertRaises(ValueError):
            client = connectwise.Client(base_url="")
            client.company.configurations.get()

    def test_invalid_token(self):
        with self.assertRaises(Exception):
            client=connectwise.Client(base_url="", auth_token="Invalid Token")
            client.company.configurations.get()

    def test_generate_auth(self):
        client = connectwise.Client(base_url="", auth_token="Invalid Token")
        self.assertEqual('QUFBK1RFU1QxOlRFU1Qy', client._generate_auth('AAA', 'TEST1', 'TEST2'))

    def test_condition_string(self):
        client = connectwise.Client(base_url="", auth_token="Invalid Token")
        new_str = ""
        new_str = client._add_condition(new_str, 'Param1', 'Value1')
        self.assertEqual('Param1="Value1"', new_str)
        new_str = client._add_condition(new_str, 'Param2', 'Value2')
        self.assertEqual('Param1="Value1" and Param2="Value2"', new_str)
        new_str = client._add_condition(new_str, 'Param3', 'Value3')
        self.assertEqual('Param1="Value1" and Param2="Value2" and Param3="Value3"', new_str)