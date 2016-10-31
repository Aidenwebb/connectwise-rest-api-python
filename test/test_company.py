import unittest

import connectwise
from connectwise import client as _client
import test as _test

class DataTests(_test.TestCase):

    def setUp(self):
        auth = ""
        site = ''

        self.client = connectwise.client.Client(base_url=site, auth_token=auth)

    def test_get_functions(self):
        self.assertEqual(200, self.client.company.configurations.get(self.client).status_code)
        self.assertEqual(200, self.client.company.companies.get(self.client).status_code)
        self.assertEqual(200, self.client.company.contacts.get(self.client).status_code)
        self.assertEqual(200, self.client.service.tickets.get(self.client).status_code)
