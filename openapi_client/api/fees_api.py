# coding: utf-8

"""
    SBC Pay API Reference

    BC Registries Pay API reference documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FeesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def calculate_fees(self, corp_type, filing_type_code, **kwargs):  # noqa: E501
        """Calculate Fees  # noqa: E501

        Calculate Fees on the filing type for corp type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.calculate_fees(corp_type, filing_type_code, async_req=True)
        >>> result = thread.get()

        :param corp_type: Corp Type (required)
        :type corp_type: str
        :param filing_type_code: Filing type code (required)
        :type filing_type_code: str
        :param jurisdiction: Jurisdiction or Province code
        :type jurisdiction: str
        :param date: Date on which the filing rates are applicable
        :type date: str
        :param priority: Indicator if priority fees are applicable
        :type priority: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Fee
        """
        kwargs['_return_http_data_only'] = True
        return self.calculate_fees_with_http_info(corp_type, filing_type_code, **kwargs)  # noqa: E501

    def calculate_fees_with_http_info(self, corp_type, filing_type_code, **kwargs):  # noqa: E501
        """Calculate Fees  # noqa: E501

        Calculate Fees on the filing type for corp type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.calculate_fees_with_http_info(corp_type, filing_type_code, async_req=True)
        >>> result = thread.get()

        :param corp_type: Corp Type (required)
        :type corp_type: str
        :param filing_type_code: Filing type code (required)
        :type filing_type_code: str
        :param jurisdiction: Jurisdiction or Province code
        :type jurisdiction: str
        :param date: Date on which the filing rates are applicable
        :type date: str
        :param priority: Indicator if priority fees are applicable
        :type priority: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Fee, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'corp_type',
            'filing_type_code',
            'jurisdiction',
            'date',
            'priority'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method calculate_fees" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'corp_type' is set
        if self.api_client.client_side_validation and ('corp_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['corp_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `corp_type` when calling `calculate_fees`")  # noqa: E501
        # verify the required parameter 'filing_type_code' is set
        if self.api_client.client_side_validation and ('filing_type_code' not in local_var_params or  # noqa: E501
                                                        local_var_params['filing_type_code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `filing_type_code` when calling `calculate_fees`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'corp_type' in local_var_params:
            path_params['corp_type'] = local_var_params['corp_type']  # noqa: E501
        if 'filing_type_code' in local_var_params:
            path_params['filing_type_code'] = local_var_params['filing_type_code']  # noqa: E501

        query_params = []
        if 'jurisdiction' in local_var_params and local_var_params['jurisdiction'] is not None:  # noqa: E501
            query_params.append(('jurisdiction', local_var_params['jurisdiction']))  # noqa: E501
        if 'date' in local_var_params and local_var_params['date'] is not None:  # noqa: E501
            query_params.append(('date', local_var_params['date']))  # noqa: E501
        if 'priority' in local_var_params and local_var_params['priority'] is not None:  # noqa: E501
            query_params.append(('priority', local_var_params['priority']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/fees/{corp_type}/{filing_type_code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Fee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
