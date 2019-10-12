"""Tests for 1cloud authenticator"""

import os
import unittest

import json
import mock
import requests

from certbot import errors
from certbot.plugins import dns_test_common
from certbot.plugins.dns_test_common import DOMAIN
from certbot.tests import util as test_util

TOKEN = 'foobar'

HTTP_ERROR = requests.exceptions.RequestException()


class AuthenticatorTest(test_util.TempDirTestCase, dns_test_common.BaseAuthenticatorTest):

    def setUp(self):
        from certbot_1cloud.dns import Authenticator

        super(AuthenticatorTest, self).setUp()

        path = os.path.join(self.tempdir, '1cloud.ini')
        dns_test_common.write({'1cloud_token': TOKEN}, path)

        k = {
            '1cloud_credentials': path,
            '1cloud_propagation_seconds': 0
        }
        self.config = mock.MagicMock(**k)
        self.auth = Authenticator(self.config, '1cloud')
        self.mock_client = mock.MagicMock()
        self.auth._get_1cloud_client = mock.MagicMock(
            return_value=self.mock_client)

    def test_perform(self):
        self.auth.perform([self.achall])

        expected = [mock.call.add_txt_record(
            '_acme-challenge.' + DOMAIN, mock.ANY)]
        self.assertEqual(expected, self.mock_client.mock_calls)

    def test_cleanup(self):
        self.auth._attempt_cleanup = True
        self.auth.cleanup([self.achall])

        expected = [mock.call.del_txt_record(
            '_acme-challenge.' + DOMAIN, mock.ANY)]
        self.assertEqual(expected, self.mock_client.mock_calls)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
