# coding: utf-8

"""
    SBC Pay API Reference

    BC Registries Pay API reference documentation  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PaymentRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'payment_info': 'list[PaymentInfo]',
        'filing_info': 'list[FilingInfo]',
        'business_info': 'list[BusinessInfo]'
    }

    attribute_map = {
        'payment_info': 'paymentInfo',
        'filing_info': 'filingInfo',
        'business_info': 'businessInfo'
    }

    def __init__(self, payment_info=None, filing_info=None, business_info=None, local_vars_configuration=None):  # noqa: E501
        """PaymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment_info = None
        self._filing_info = None
        self._business_info = None
        self.discriminator = None

        if payment_info is not None:
            self.payment_info = payment_info
        if filing_info is not None:
            self.filing_info = filing_info
        if business_info is not None:
            self.business_info = business_info

    @property
    def payment_info(self):
        """Gets the payment_info of this PaymentRequest.  # noqa: E501


        :return: The payment_info of this PaymentRequest.  # noqa: E501
        :rtype: list[PaymentInfo]
        """
        return self._payment_info

    @payment_info.setter
    def payment_info(self, payment_info):
        """Sets the payment_info of this PaymentRequest.


        :param payment_info: The payment_info of this PaymentRequest.  # noqa: E501
        :type payment_info: list[PaymentInfo]
        """

        self._payment_info = payment_info

    @property
    def filing_info(self):
        """Gets the filing_info of this PaymentRequest.  # noqa: E501


        :return: The filing_info of this PaymentRequest.  # noqa: E501
        :rtype: list[FilingInfo]
        """
        return self._filing_info

    @filing_info.setter
    def filing_info(self, filing_info):
        """Sets the filing_info of this PaymentRequest.


        :param filing_info: The filing_info of this PaymentRequest.  # noqa: E501
        :type filing_info: list[FilingInfo]
        """

        self._filing_info = filing_info

    @property
    def business_info(self):
        """Gets the business_info of this PaymentRequest.  # noqa: E501


        :return: The business_info of this PaymentRequest.  # noqa: E501
        :rtype: list[BusinessInfo]
        """
        return self._business_info

    @business_info.setter
    def business_info(self, business_info):
        """Sets the business_info of this PaymentRequest.


        :param business_info: The business_info of this PaymentRequest.  # noqa: E501
        :type business_info: list[BusinessInfo]
        """

        self._business_info = business_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentRequest):
            return True

        return self.to_dict() != other.to_dict()
