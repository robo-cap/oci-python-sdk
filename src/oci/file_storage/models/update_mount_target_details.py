# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMountTargetDetails(object):
    """
    Details for updating the mount target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMountTargetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMountTargetDetails.
        :type display_name: str

        :param idmap_type:
            The value to assign to the idmap_type property of this UpdateMountTargetDetails.
        :type idmap_type: str

        :param ldap_idmap:
            The value to assign to the ldap_idmap property of this UpdateMountTargetDetails.
        :type ldap_idmap: oci.file_storage.models.UpdateLdapIdmapDetails

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateMountTargetDetails.
        :type nsg_ids: list[str]

        :param kerberos:
            The value to assign to the kerberos property of this UpdateMountTargetDetails.
        :type kerberos: oci.file_storage.models.UpdateKerberosDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMountTargetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMountTargetDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'idmap_type': 'str',
            'ldap_idmap': 'UpdateLdapIdmapDetails',
            'nsg_ids': 'list[str]',
            'kerberos': 'UpdateKerberosDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'idmap_type': 'idmapType',
            'ldap_idmap': 'ldapIdmap',
            'nsg_ids': 'nsgIds',
            'kerberos': 'kerberos',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._idmap_type = None
        self._ldap_idmap = None
        self._nsg_ids = None
        self._kerberos = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMountTargetDetails.
        A user-friendly name. Does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :return: The display_name of this UpdateMountTargetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMountTargetDetails.
        A user-friendly name. Does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My mount target`


        :param display_name: The display_name of this UpdateMountTargetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def idmap_type(self):
        """
        Gets the idmap_type of this UpdateMountTargetDetails.
        The method used to map a Unix UID to secondary groups, if any.


        :return: The idmap_type of this UpdateMountTargetDetails.
        :rtype: str
        """
        return self._idmap_type

    @idmap_type.setter
    def idmap_type(self, idmap_type):
        """
        Sets the idmap_type of this UpdateMountTargetDetails.
        The method used to map a Unix UID to secondary groups, if any.


        :param idmap_type: The idmap_type of this UpdateMountTargetDetails.
        :type: str
        """
        self._idmap_type = idmap_type

    @property
    def ldap_idmap(self):
        """
        Gets the ldap_idmap of this UpdateMountTargetDetails.

        :return: The ldap_idmap of this UpdateMountTargetDetails.
        :rtype: oci.file_storage.models.UpdateLdapIdmapDetails
        """
        return self._ldap_idmap

    @ldap_idmap.setter
    def ldap_idmap(self, ldap_idmap):
        """
        Sets the ldap_idmap of this UpdateMountTargetDetails.

        :param ldap_idmap: The ldap_idmap of this UpdateMountTargetDetails.
        :type: oci.file_storage.models.UpdateLdapIdmapDetails
        """
        self._ldap_idmap = ldap_idmap

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateMountTargetDetails.
        A list of Network Security Group `OCIDs`__ associated with this mount target.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the mount target from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this UpdateMountTargetDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateMountTargetDetails.
        A list of Network Security Group `OCIDs`__ associated with this mount target.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the mount target from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this UpdateMountTargetDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def kerberos(self):
        """
        Gets the kerberos of this UpdateMountTargetDetails.

        :return: The kerberos of this UpdateMountTargetDetails.
        :rtype: oci.file_storage.models.UpdateKerberosDetails
        """
        return self._kerberos

    @kerberos.setter
    def kerberos(self, kerberos):
        """
        Sets the kerberos of this UpdateMountTargetDetails.

        :param kerberos: The kerberos of this UpdateMountTargetDetails.
        :type: oci.file_storage.models.UpdateKerberosDetails
        """
        self._kerberos = kerberos

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMountTargetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateMountTargetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMountTargetDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateMountTargetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMountTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateMountTargetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMountTargetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateMountTargetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
