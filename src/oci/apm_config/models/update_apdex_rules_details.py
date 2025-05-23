# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210201

from .update_config_details import UpdateConfigDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateApdexRulesDetails(UpdateConfigDetails):
    """
    The set of Apdex rules to be used in Apdex computation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateApdexRulesDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_config.models.UpdateApdexRulesDetails.config_type` attribute
        of this class is ``APDEX`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this UpdateApdexRulesDetails.
            Allowed values for this property are: "SPAN_FILTER", "METRIC_GROUP", "APDEX", "OPTIONS"
        :type config_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateApdexRulesDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateApdexRulesDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param rules:
            The value to assign to the rules property of this UpdateApdexRulesDetails.
        :type rules: list[oci.apm_config.models.Apdex]

        :param display_name:
            The value to assign to the display_name property of this UpdateApdexRulesDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'config_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'rules': 'list[Apdex]',
            'display_name': 'str'
        }
        self.attribute_map = {
            'config_type': 'configType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'rules': 'rules',
            'display_name': 'displayName'
        }
        self._config_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._rules = None
        self._display_name = None
        self._config_type = 'APDEX'

    @property
    def rules(self):
        """
        **[Required]** Gets the rules of this UpdateApdexRulesDetails.

        :return: The rules of this UpdateApdexRulesDetails.
        :rtype: list[oci.apm_config.models.Apdex]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this UpdateApdexRulesDetails.

        :param rules: The rules of this UpdateApdexRulesDetails.
        :type: list[oci.apm_config.models.Apdex]
        """
        self._rules = rules

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateApdexRulesDetails.
        The name by which a configuration entity is displayed to the end user.


        :return: The display_name of this UpdateApdexRulesDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateApdexRulesDetails.
        The name by which a configuration entity is displayed to the end user.


        :param display_name: The display_name of this UpdateApdexRulesDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
