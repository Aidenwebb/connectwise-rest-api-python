"""
Core client functoinality, common across all API requests
"""

import base64

import requests

try: # Python 3
    from urllib.parse import urlencode
except ImportError: # Python 2
    from urllib import urlencode

class Client(object):

    """Performs requests to the Connectwise API web services"""

    def __init__(self, base_url, auth_token=None, company_identifier=None, public_key=None, private_key=None):

        """

        :param base_url: Base URL of your connectwise installation. eg: connectwise.exampleit.com
        :type base_url: string

        :param auth_token: Required, unless "company identifer", "public_key" and "private_key" are set,
            A base 64 hash of your connectwise Company ID, public key and private key in format: companyID+public_key:private_key
        :type auth_token: string

        :param company_identifier: Required, unless "auth_token" is set. Your company ID as entered in the "Company" field when logging in to the connectwise Webclient.
        :type company_identifier: string

        :param public_key: Required, unless "auth_token" is set. Your public_key from your Connectwise User API
        :type public_key: string

        :param private_key: Required, unless "auth_token" is set. Your private_key from your Connectwise User API
        :type private_key: string
        """

        if not auth_token and not (company_identifier and public_key and private_key):
            raise ValueError("Must provide Auth Token or company identifier, public key and private key")

        if auth_token is None:
            self.auth_token = self._generate_auth(company_identifier, public_key, private_key)
        else:
            self.auth_token = auth_token

        self._default_headers = {"Authorization": "Basic %s" % auth_token,
                                 "Content-Type": "application/json"}
        self.site = base_url
        self.api_url = "https://{site}/v4_6_release/apis/3.0".format(site=self.site)

        self.requests_kwargs = {}
        self.requests_kwargs.update({
            "headers": {"Authorization": "Basic %s" % auth_token,
                                 "Content-Type": "application/json"},
            "verify": True, # NOTE(cbro): verify SSL certs.
        })

        self.connection = requests.Session()
        self.connection.headers = self._default_headers

    def _get(self, url, parameters):
        full_path = self.api_url + url
        resp = self.connection.get(full_path, params=parameters)
        print(resp.url)
        return resp

    def _post(self, url, json):
        full_path = self.api_url + url
        return self.connection.post(full_path, json=json)

    def _patch(self, url, json):
        full_path = self.api_url + url
        return self.connection.patch(full_path, json=json)

    def _generate_auth(self, company_id, public_key, private_key):
        token = "{}+{}:{}".format(company_id, public_key, private_key)
        token = base64.b64encode(bytes(token, 'utf-8'))
        print(token)
        token = token.decode('utf-8')
        return token

    def _generate_auth_url(self, path, params):
        """Returns the path and a query string portion of the request URL, first adding any necessary parameters.

        """

        # Deterministic ordering through sorting by key
        # Useful for tests, and in the furture, any caching.
        if type(params) is dict:
            params = sorted(params.items())
        else:
            params = params[:]  # Take a copy

        return path + "?" + urlencode(params)

    def _add_condition(self, string, condition_name, condition_value):
        if string == '':
            if type(condition_value) is int or type(condition_value) is bool:
                result = '{}={}'.format(condition_name, condition_value)
            elif type(condition_value) is str:
                result = '{}="{}"'.format(condition_name, condition_value)
        else:
            if type(condition_value) is int or type(condition_value) is bool:
                result = '{} and {}={}'.format(string, condition_name, condition_value)
            elif type(condition_value) is str:
                result = '{} and {}="{}"'.format(string, condition_name, condition_value)
        print(result)
        return result

    def _get_contact_id(self, contact_name, company_identifier):
        first_name = contact_name.split(' ')[0]
        last_name = contact_name.split(' ')[1]
        contact = self.company.contacts.get(self, first_name=first_name, last_name=last_name, company_identifier=company_identifier).json()
        return contact[0]['id']

from connectwise import company
from connectwise import service
Client.company = company
Client.service = service


