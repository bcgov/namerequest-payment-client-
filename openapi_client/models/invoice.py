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


class Invoice(object):
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
        'links': 'list[Links]',
        'id': 'int',
        'created_by': 'str',
        'created_name': 'str',
        'created_on': 'str',
        'updated_name': 'str',
        'updated_on': 'str',
        'line_items': 'list[LineItem]',
        'paid': 'float',
        'refund': 'float',
        'service_fees': 'float',
        'total': 'float',
        'references': 'list[InvoiceReference]',
        'status_code': 'str'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'created_by': 'createdBy',
        'created_name': 'createdName',
        'created_on': 'createdOn',
        'updated_name': 'updatedName',
        'updated_on': 'updatedOn',
        'line_items': 'lineItems',
        'paid': 'paid',
        'refund': 'refund',
        'service_fees': 'serviceFees',
        'total': 'total',
        'references': 'references',
        'status_code': 'statusCode'
    }

    def __init__(self, links=None, id=None, created_by=None, created_name=None, created_on=None, updated_name=None, updated_on=None, line_items=None, paid=None, refund=None, service_fees=None, total=None, references=None, status_code=None, local_vars_configuration=None):  # noqa: E501
        """Invoice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._links = None
        self._id = None
        self._created_by = None
        self._created_name = None
        self._created_on = None
        self._updated_name = None
        self._updated_on = None
        self._line_items = None
        self._paid = None
        self._refund = None
        self._service_fees = None
        self._total = None
        self._references = None
        self._status_code = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_name is not None:
            self.created_name = created_name
        if created_on is not None:
            self.created_on = created_on
        if updated_name is not None:
            self.updated_name = updated_name
        if updated_on is not None:
            self.updated_on = updated_on
        if line_items is not None:
            self.line_items = line_items
        if paid is not None:
            self.paid = paid
        if refund is not None:
            self.refund = refund
        if service_fees is not None:
            self.service_fees = service_fees
        if total is not None:
            self.total = total
        if references is not None:
            self.references = references
        if status_code is not None:
            self.status_code = status_code

    @property
    def links(self):
        """Gets the links of this Invoice.  # noqa: E501


        :return: The links of this Invoice.  # noqa: E501
        :rtype: list[Links]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Invoice.


        :param links: The links of this Invoice.  # noqa: E501
        :type links: list[Links]
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this Invoice.  # noqa: E501

        Unique identifier for invoice  # noqa: E501

        :return: The id of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invoice.

        Unique identifier for invoice  # noqa: E501

        :param id: The id of this Invoice.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this Invoice.  # noqa: E501

        username of the account  # noqa: E501

        :return: The created_by of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Invoice.

        username of the account  # noqa: E501

        :param created_by: The created_by of this Invoice.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def created_name(self):
        """Gets the created_name of this Invoice.  # noqa: E501

        username of the account  # noqa: E501

        :return: The created_name of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._created_name

    @created_name.setter
    def created_name(self, created_name):
        """Sets the created_name of this Invoice.

        username of the account  # noqa: E501

        :param created_name: The created_name of this Invoice.  # noqa: E501
        :type created_name: str
        """

        self._created_name = created_name

    @property
    def created_on(self):
        """Gets the created_on of this Invoice.  # noqa: E501

        invoice created date  # noqa: E501

        :return: The created_on of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Invoice.

        invoice created date  # noqa: E501

        :param created_on: The created_on of this Invoice.  # noqa: E501
        :type created_on: str
        """

        self._created_on = created_on

    @property
    def updated_name(self):
        """Gets the updated_name of this Invoice.  # noqa: E501

        username of the account  # noqa: E501

        :return: The updated_name of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._updated_name

    @updated_name.setter
    def updated_name(self, updated_name):
        """Sets the updated_name of this Invoice.

        username of the account  # noqa: E501

        :param updated_name: The updated_name of this Invoice.  # noqa: E501
        :type updated_name: str
        """

        self._updated_name = updated_name

    @property
    def updated_on(self):
        """Gets the updated_on of this Invoice.  # noqa: E501

        invoice update date  # noqa: E501

        :return: The updated_on of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Invoice.

        invoice update date  # noqa: E501

        :param updated_on: The updated_on of this Invoice.  # noqa: E501
        :type updated_on: str
        """

        self._updated_on = updated_on

    @property
    def line_items(self):
        """Gets the line_items of this Invoice.  # noqa: E501


        :return: The line_items of this Invoice.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Invoice.


        :param line_items: The line_items of this Invoice.  # noqa: E501
        :type line_items: list[LineItem]
        """

        self._line_items = line_items

    @property
    def paid(self):
        """Gets the paid of this Invoice.  # noqa: E501

        amount paid  # noqa: E501

        :return: The paid of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """Sets the paid of this Invoice.

        amount paid  # noqa: E501

        :param paid: The paid of this Invoice.  # noqa: E501
        :type paid: float
        """

        self._paid = paid

    @property
    def refund(self):
        """Gets the refund of this Invoice.  # noqa: E501

        refund amount  # noqa: E501

        :return: The refund of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this Invoice.

        refund amount  # noqa: E501

        :param refund: The refund of this Invoice.  # noqa: E501
        :type refund: float
        """

        self._refund = refund

    @property
    def service_fees(self):
        """Gets the service_fees of this Invoice.  # noqa: E501

        service fees amount  # noqa: E501

        :return: The service_fees of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._service_fees

    @service_fees.setter
    def service_fees(self, service_fees):
        """Sets the service_fees of this Invoice.

        service fees amount  # noqa: E501

        :param service_fees: The service_fees of this Invoice.  # noqa: E501
        :type service_fees: float
        """

        self._service_fees = service_fees

    @property
    def total(self):
        """Gets the total of this Invoice.  # noqa: E501

        total amount  # noqa: E501

        :return: The total of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Invoice.

        total amount  # noqa: E501

        :param total: The total of this Invoice.  # noqa: E501
        :type total: float
        """

        self._total = total

    @property
    def references(self):
        """Gets the references of this Invoice.  # noqa: E501


        :return: The references of this Invoice.  # noqa: E501
        :rtype: list[InvoiceReference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this Invoice.


        :param references: The references of this Invoice.  # noqa: E501
        :type references: list[InvoiceReference]
        """

        self._references = references

    @property
    def status_code(self):
        """Gets the status_code of this Invoice.  # noqa: E501

        Status of payment.  # noqa: E501

        :return: The status_code of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Invoice.

        Status of payment.  # noqa: E501

        :param status_code: The status_code of this Invoice.  # noqa: E501
        :type status_code: str
        """
        allowed_values = ["PAID", "DRAFT", "IN_PROGRESS", "CREATED", "COMPLETED", "PARTIAL", "FAILED", "REFUNDED", "CANCELLED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

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
        if not isinstance(other, Invoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invoice):
            return True

        return self.to_dict() != other.to_dict()
