# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.images import Images

class TestImages(unittest.TestCase):
    """Images unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Images:
        """Test Images
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Images`
        """
        model = Images()
        if include_optional:
            return Images(
                status = True,
                message = '',
                images = [
                    hyperstack.models.image_get_response.ImageGetResponse(
                        region_name = '', 
                        type = '', 
                        logo = '', 
                        images = [
                            hyperstack.models.image_fields.ImageFields(
                                id = 56, 
                                name = '', 
                                region_name = '', 
                                type = '', 
                                version = '', 
                                size = 56, 
                                display_size = '', 
                                description = '', 
                                labels = [
                                    hyperstack.models.lable_resonse.LableResonse(
                                        id = 56, 
                                        label = '', )
                                    ], 
                                is_public = True, )
                            ], )
                    ]
            )
        else:
            return Images(
        )
        """

    def testImages(self):
        """Test Images"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
