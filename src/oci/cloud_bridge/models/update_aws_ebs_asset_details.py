# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220509

from .update_asset_details import UpdateAssetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAwsEbsAssetDetails(UpdateAssetDetails):
    """
    The information of AWS EBS asset to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAwsEbsAssetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_bridge.models.UpdateAwsEbsAssetDetails.asset_type` attribute
        of this class is ``AWS_EBS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAwsEbsAssetDetails.
        :type display_name: str

        :param asset_type:
            The value to assign to the asset_type property of this UpdateAwsEbsAssetDetails.
            Allowed values for this property are: "VMWARE_VM", "VM", "AWS_EC2", "AWS_EBS"
        :type asset_type: str

        :param asset_source_ids:
            The value to assign to the asset_source_ids property of this UpdateAwsEbsAssetDetails.
        :type asset_source_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAwsEbsAssetDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAwsEbsAssetDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param aws_ebs:
            The value to assign to the aws_ebs property of this UpdateAwsEbsAssetDetails.
        :type aws_ebs: oci.cloud_bridge.models.AwsEbsProperties

        """
        self.swagger_types = {
            'display_name': 'str',
            'asset_type': 'str',
            'asset_source_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'aws_ebs': 'AwsEbsProperties'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'asset_type': 'assetType',
            'asset_source_ids': 'assetSourceIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'aws_ebs': 'awsEbs'
        }
        self._display_name = None
        self._asset_type = None
        self._asset_source_ids = None
        self._freeform_tags = None
        self._defined_tags = None
        self._aws_ebs = None
        self._asset_type = 'AWS_EBS'

    @property
    def aws_ebs(self):
        """
        Gets the aws_ebs of this UpdateAwsEbsAssetDetails.

        :return: The aws_ebs of this UpdateAwsEbsAssetDetails.
        :rtype: oci.cloud_bridge.models.AwsEbsProperties
        """
        return self._aws_ebs

    @aws_ebs.setter
    def aws_ebs(self, aws_ebs):
        """
        Sets the aws_ebs of this UpdateAwsEbsAssetDetails.

        :param aws_ebs: The aws_ebs of this UpdateAwsEbsAssetDetails.
        :type: oci.cloud_bridge.models.AwsEbsProperties
        """
        self._aws_ebs = aws_ebs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
