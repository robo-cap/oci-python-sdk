# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericRestApiAttributes(object):
    """
    Generic rest api specific attributes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GenericRestApiAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param server_url:
            The value to assign to the server_url property of this GenericRestApiAttributes.
        :type server_url: str

        """
        self.swagger_types = {
            'server_url': 'str'
        }
        self.attribute_map = {
            'server_url': 'serverUrl'
        }
        self._server_url = None

    @property
    def server_url(self):
        """
        Gets the server_url of this GenericRestApiAttributes.
        The server URL serving operation.


        :return: The server_url of this GenericRestApiAttributes.
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """
        Sets the server_url of this GenericRestApiAttributes.
        The server URL serving operation.


        :param server_url: The server_url of this GenericRestApiAttributes.
        :type: str
        """
        self._server_url = server_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
