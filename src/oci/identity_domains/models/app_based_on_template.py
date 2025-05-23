# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppBasedOnTemplate(object):
    """
    Application template on which the application is based.

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: immutable
    - required: true
    - returned: default
    - type: complex
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppBasedOnTemplate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppBasedOnTemplate.
        :type value: str

        :param ref:
            The value to assign to the ref property of this AppBasedOnTemplate.
        :type ref: str

        :param last_modified:
            The value to assign to the last_modified property of this AppBasedOnTemplate.
        :type last_modified: str

        :param well_known_id:
            The value to assign to the well_known_id property of this AppBasedOnTemplate.
        :type well_known_id: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'last_modified': 'str',
            'well_known_id': 'str'
        }
        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'last_modified': 'lastModified',
            'well_known_id': 'wellKnownId'
        }
        self._value = None
        self._ref = None
        self._last_modified = None
        self._well_known_id = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AppBasedOnTemplate.
        Identifier of the application template.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :return: The value of this AppBasedOnTemplate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppBasedOnTemplate.
        Identifier of the application template.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: true
         - returned: always
         - type: string
         - uniqueness: none


        :param value: The value of this AppBasedOnTemplate.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this AppBasedOnTemplate.
        URI of the application template.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AppBasedOnTemplate.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AppBasedOnTemplate.
        URI of the application template.

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AppBasedOnTemplate.
        :type: str
        """
        self._ref = ref

    @property
    def last_modified(self):
        """
        Gets the last_modified of this AppBasedOnTemplate.
        The most recent DateTime that the appTemplate on which the application based upon is updated. The attribute MUST be a DateTime.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The last_modified of this AppBasedOnTemplate.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this AppBasedOnTemplate.
        The most recent DateTime that the appTemplate on which the application based upon is updated. The attribute MUST be a DateTime.

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param last_modified: The last_modified of this AppBasedOnTemplate.
        :type: str
        """
        self._last_modified = last_modified

    @property
    def well_known_id(self):
        """
        Gets the well_known_id of this AppBasedOnTemplate.
        Unique Well-known identifier used to reference app template.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The well_known_id of this AppBasedOnTemplate.
        :rtype: str
        """
        return self._well_known_id

    @well_known_id.setter
    def well_known_id(self, well_known_id):
        """
        Sets the well_known_id of this AppBasedOnTemplate.
        Unique Well-known identifier used to reference app template.

        **Added In:** 18.2.6

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param well_known_id: The well_known_id of this AppBasedOnTemplate.
        :type: str
        """
        self._well_known_id = well_known_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
