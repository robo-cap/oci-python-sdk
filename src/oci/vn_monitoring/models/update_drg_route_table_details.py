# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgRouteTableDetails(object):
    """
    Details used in a request to update a DRG route table.

    You can't assign a table to a virtual circuit or IPSec tunnel attachment if there is a static route rule for an RPC attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgRouteTableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDrgRouteTableDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateDrgRouteTableDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDrgRouteTableDetails.
        :type freeform_tags: dict(str, str)

        :param import_drg_route_distribution_id:
            The value to assign to the import_drg_route_distribution_id property of this UpdateDrgRouteTableDetails.
        :type import_drg_route_distribution_id: str

        :param is_ecmp_enabled:
            The value to assign to the is_ecmp_enabled property of this UpdateDrgRouteTableDetails.
        :type is_ecmp_enabled: bool

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'import_drg_route_distribution_id': 'str',
            'is_ecmp_enabled': 'bool'
        }
        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'import_drg_route_distribution_id': 'importDrgRouteDistributionId',
            'is_ecmp_enabled': 'isEcmpEnabled'
        }
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._import_drg_route_distribution_id = None
        self._is_ecmp_enabled = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDrgRouteTableDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDrgRouteTableDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDrgRouteTableDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDrgRouteTableDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrgRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this UpdateDrgRouteTableDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrgRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDrgRouteTableDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDrgRouteTableDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDrgRouteTableDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDrgRouteTableDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDrgRouteTableDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def import_drg_route_distribution_id(self):
        """
        Gets the import_drg_route_distribution_id of this UpdateDrgRouteTableDetails.
        The `OCID`__ of the import route distribution used to specify how incoming route advertisements through
        referenced attachements are inserted into the DRG route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The import_drg_route_distribution_id of this UpdateDrgRouteTableDetails.
        :rtype: str
        """
        return self._import_drg_route_distribution_id

    @import_drg_route_distribution_id.setter
    def import_drg_route_distribution_id(self, import_drg_route_distribution_id):
        """
        Sets the import_drg_route_distribution_id of this UpdateDrgRouteTableDetails.
        The `OCID`__ of the import route distribution used to specify how incoming route advertisements through
        referenced attachements are inserted into the DRG route table.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param import_drg_route_distribution_id: The import_drg_route_distribution_id of this UpdateDrgRouteTableDetails.
        :type: str
        """
        self._import_drg_route_distribution_id = import_drg_route_distribution_id

    @property
    def is_ecmp_enabled(self):
        """
        Gets the is_ecmp_enabled of this UpdateDrgRouteTableDetails.
        If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
        your on-prem networks, set this value to true on the route table.


        :return: The is_ecmp_enabled of this UpdateDrgRouteTableDetails.
        :rtype: bool
        """
        return self._is_ecmp_enabled

    @is_ecmp_enabled.setter
    def is_ecmp_enabled(self, is_ecmp_enabled):
        """
        Sets the is_ecmp_enabled of this UpdateDrgRouteTableDetails.
        If you want traffic to be routed using ECMP across your virtual circuits or IPSec tunnels to
        your on-prem networks, set this value to true on the route table.


        :param is_ecmp_enabled: The is_ecmp_enabled of this UpdateDrgRouteTableDetails.
        :type: bool
        """
        self._is_ecmp_enabled = is_ecmp_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
