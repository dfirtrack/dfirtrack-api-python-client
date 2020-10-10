# coding: utf-8

"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: 0.4.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import dfirtrackapi_client
from dfirtrackapi_client.models.artifactstatus import Artifactstatus  # noqa: E501
from dfirtrackapi_client.rest import ApiException

class TestArtifactstatus(unittest.TestCase):
    """Artifactstatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Artifactstatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = dfirtrackapi_client.models.artifactstatus.Artifactstatus()  # noqa: E501
        if include_optional :
            return Artifactstatus(
                artifactstatus_name = '0'
            )
        else :
            return Artifactstatus(
                artifactstatus_name = '0',
        )

    def testArtifactstatus(self):
        """Test Artifactstatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()