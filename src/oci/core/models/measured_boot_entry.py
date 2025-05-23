# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MeasuredBootEntry(object):
    """
    One Trusted Platform Module (TPM) Platform Configuration Register (PCR) entry. The entry might be measured during boot,
    or specified in a policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MeasuredBootEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pcr_index:
            The value to assign to the pcr_index property of this MeasuredBootEntry.
        :type pcr_index: str

        :param value:
            The value to assign to the value property of this MeasuredBootEntry.
        :type value: str

        :param hash_algorithm:
            The value to assign to the hash_algorithm property of this MeasuredBootEntry.
        :type hash_algorithm: str

        """
        self.swagger_types = {
            'pcr_index': 'str',
            'value': 'str',
            'hash_algorithm': 'str'
        }
        self.attribute_map = {
            'pcr_index': 'pcrIndex',
            'value': 'value',
            'hash_algorithm': 'hashAlgorithm'
        }
        self._pcr_index = None
        self._value = None
        self._hash_algorithm = None

    @property
    def pcr_index(self):
        """
        Gets the pcr_index of this MeasuredBootEntry.
        The index of the policy.


        :return: The pcr_index of this MeasuredBootEntry.
        :rtype: str
        """
        return self._pcr_index

    @pcr_index.setter
    def pcr_index(self, pcr_index):
        """
        Sets the pcr_index of this MeasuredBootEntry.
        The index of the policy.


        :param pcr_index: The pcr_index of this MeasuredBootEntry.
        :type: str
        """
        self._pcr_index = pcr_index

    @property
    def value(self):
        """
        Gets the value of this MeasuredBootEntry.
        The hashed PCR value.


        :return: The value of this MeasuredBootEntry.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MeasuredBootEntry.
        The hashed PCR value.


        :param value: The value of this MeasuredBootEntry.
        :type: str
        """
        self._value = value

    @property
    def hash_algorithm(self):
        """
        Gets the hash_algorithm of this MeasuredBootEntry.
        The type of algorithm used to calculate the hash.


        :return: The hash_algorithm of this MeasuredBootEntry.
        :rtype: str
        """
        return self._hash_algorithm

    @hash_algorithm.setter
    def hash_algorithm(self, hash_algorithm):
        """
        Sets the hash_algorithm of this MeasuredBootEntry.
        The type of algorithm used to calculate the hash.


        :param hash_algorithm: The hash_algorithm of this MeasuredBootEntry.
        :type: str
        """
        self._hash_algorithm = hash_algorithm

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
