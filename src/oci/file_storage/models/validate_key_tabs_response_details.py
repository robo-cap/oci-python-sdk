# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidateKeyTabsResponseDetails(object):
    """
    Validate keytabs response details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValidateKeyTabsResponseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param current_kerberos_keytab_entries:
            The value to assign to the current_kerberos_keytab_entries property of this ValidateKeyTabsResponseDetails.
        :type current_kerberos_keytab_entries: list[oci.file_storage.models.KerberosKeytabEntry]

        :param backup_kerberos_keytab_entries:
            The value to assign to the backup_kerberos_keytab_entries property of this ValidateKeyTabsResponseDetails.
        :type backup_kerberos_keytab_entries: list[oci.file_storage.models.KerberosKeytabEntry]

        """
        self.swagger_types = {
            'current_kerberos_keytab_entries': 'list[KerberosKeytabEntry]',
            'backup_kerberos_keytab_entries': 'list[KerberosKeytabEntry]'
        }
        self.attribute_map = {
            'current_kerberos_keytab_entries': 'currentKerberosKeytabEntries',
            'backup_kerberos_keytab_entries': 'backupKerberosKeytabEntries'
        }
        self._current_kerberos_keytab_entries = None
        self._backup_kerberos_keytab_entries = None

    @property
    def current_kerberos_keytab_entries(self):
        """
        **[Required]** Gets the current_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        An array of keytab entries (principal, encryptionType, keyVersionNumber).


        :return: The current_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        :rtype: list[oci.file_storage.models.KerberosKeytabEntry]
        """
        return self._current_kerberos_keytab_entries

    @current_kerberos_keytab_entries.setter
    def current_kerberos_keytab_entries(self, current_kerberos_keytab_entries):
        """
        Sets the current_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        An array of keytab entries (principal, encryptionType, keyVersionNumber).


        :param current_kerberos_keytab_entries: The current_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        :type: list[oci.file_storage.models.KerberosKeytabEntry]
        """
        self._current_kerberos_keytab_entries = current_kerberos_keytab_entries

    @property
    def backup_kerberos_keytab_entries(self):
        """
        Gets the backup_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        An array of keytab entries (principal, encryptionType, keyVersionNumber).


        :return: The backup_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        :rtype: list[oci.file_storage.models.KerberosKeytabEntry]
        """
        return self._backup_kerberos_keytab_entries

    @backup_kerberos_keytab_entries.setter
    def backup_kerberos_keytab_entries(self, backup_kerberos_keytab_entries):
        """
        Sets the backup_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        An array of keytab entries (principal, encryptionType, keyVersionNumber).


        :param backup_kerberos_keytab_entries: The backup_kerberos_keytab_entries of this ValidateKeyTabsResponseDetails.
        :type: list[oci.file_storage.models.KerberosKeytabEntry]
        """
        self._backup_kerberos_keytab_entries = backup_kerberos_keytab_entries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
