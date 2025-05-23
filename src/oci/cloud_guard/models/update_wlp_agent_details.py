# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateWlpAgentDetails(object):
    """
    On-premise resource agent update or renew certificate response resource.
    Example: `{\"certificateSignedRequest\": \"MIIGwjCCBaqgAwIBAgIVAK8hJCS/5Hu0dEMQ2ud\"}`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateWlpAgentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_signed_request:
            The value to assign to the certificate_signed_request property of this UpdateWlpAgentDetails.
        :type certificate_signed_request: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateWlpAgentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateWlpAgentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'certificate_signed_request': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'certificate_signed_request': 'certificateSignedRequest',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._certificate_signed_request = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def certificate_signed_request(self):
        """
        **[Required]** Gets the certificate_signed_request of this UpdateWlpAgentDetails.
        The updated certificate signing request


        :return: The certificate_signed_request of this UpdateWlpAgentDetails.
        :rtype: str
        """
        return self._certificate_signed_request

    @certificate_signed_request.setter
    def certificate_signed_request(self, certificate_signed_request):
        """
        Sets the certificate_signed_request of this UpdateWlpAgentDetails.
        The updated certificate signing request


        :param certificate_signed_request: The certificate_signed_request of this UpdateWlpAgentDetails.
        :type: str
        """
        self._certificate_signed_request = certificate_signed_request

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateWlpAgentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :return: The freeform_tags of this UpdateWlpAgentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateWlpAgentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`

        Avoid entering confidential information.


        :param freeform_tags: The freeform_tags of this UpdateWlpAgentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateWlpAgentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateWlpAgentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateWlpAgentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateWlpAgentDetails.
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
