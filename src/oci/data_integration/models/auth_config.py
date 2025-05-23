# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200430


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthConfig(object):
    """
    Authentication configuration for Generic REST invocation.
    """

    #: A constant which can be used with the model_type property of a AuthConfig.
    #: This constant has a value of "OCI_RESOURCE_AUTH_CONFIG"
    MODEL_TYPE_OCI_RESOURCE_AUTH_CONFIG = "OCI_RESOURCE_AUTH_CONFIG"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.ResourcePrincipalAuthConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this AuthConfig.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this AuthConfig.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this AuthConfig.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param model_type:
            The value to assign to the model_type property of this AuthConfig.
            Allowed values for this property are: "OCI_RESOURCE_AUTH_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'model_type': 'str'
        }
        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'model_type': 'modelType'
        }
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._model_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'OCI_RESOURCE_AUTH_CONFIG':
            return 'ResourcePrincipalAuthConfig'
        else:
            return 'AuthConfig'

    @property
    def key(self):
        """
        Gets the key of this AuthConfig.
        Generated key that can be used in API calls to identify this object.


        :return: The key of this AuthConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AuthConfig.
        Generated key that can be used in API calls to identify this object.


        :param key: The key of this AuthConfig.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this AuthConfig.
        The model version of an object.


        :return: The model_version of this AuthConfig.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this AuthConfig.
        The model version of an object.


        :param model_version: The model_version of this AuthConfig.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this AuthConfig.

        :return: The parent_ref of this AuthConfig.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this AuthConfig.

        :param parent_ref: The parent_ref of this AuthConfig.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def model_type(self):
        """
        Gets the model_type of this AuthConfig.
        The specific authentication configuration to be used for Generic REST invocation.

        Allowed values for this property are: "OCI_RESOURCE_AUTH_CONFIG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this AuthConfig.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this AuthConfig.
        The specific authentication configuration to be used for Generic REST invocation.


        :param model_type: The model_type of this AuthConfig.
        :type: str
        """
        allowed_values = ["OCI_RESOURCE_AUTH_CONFIG"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
