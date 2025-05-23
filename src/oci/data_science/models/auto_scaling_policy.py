# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .scaling_policy import ScalingPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalingPolicy(ScalingPolicy):
    """
    The scaling policy to enable autoscaling on the model deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalingPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.AutoScalingPolicy.policy_type` attribute
        of this class is ``AUTOSCALING`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this AutoScalingPolicy.
            Allowed values for this property are: "FIXED_SIZE", "AUTOSCALING"
        :type policy_type: str

        :param cool_down_in_seconds:
            The value to assign to the cool_down_in_seconds property of this AutoScalingPolicy.
        :type cool_down_in_seconds: int

        :param is_enabled:
            The value to assign to the is_enabled property of this AutoScalingPolicy.
        :type is_enabled: bool

        :param auto_scaling_policies:
            The value to assign to the auto_scaling_policies property of this AutoScalingPolicy.
        :type auto_scaling_policies: list[oci.data_science.models.AutoScalingPolicyDetails]

        """
        self.swagger_types = {
            'policy_type': 'str',
            'cool_down_in_seconds': 'int',
            'is_enabled': 'bool',
            'auto_scaling_policies': 'list[AutoScalingPolicyDetails]'
        }
        self.attribute_map = {
            'policy_type': 'policyType',
            'cool_down_in_seconds': 'coolDownInSeconds',
            'is_enabled': 'isEnabled',
            'auto_scaling_policies': 'autoScalingPolicies'
        }
        self._policy_type = None
        self._cool_down_in_seconds = None
        self._is_enabled = None
        self._auto_scaling_policies = None
        self._policy_type = 'AUTOSCALING'

    @property
    def cool_down_in_seconds(self):
        """
        Gets the cool_down_in_seconds of this AutoScalingPolicy.
        For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions.
        The cooldown period gives the system time to stabilize before rescaling. The minimum value is 600 seconds, which
        is also the default. The cooldown period starts when the model deployment becomes ACTIVE after the scaling operation.


        :return: The cool_down_in_seconds of this AutoScalingPolicy.
        :rtype: int
        """
        return self._cool_down_in_seconds

    @cool_down_in_seconds.setter
    def cool_down_in_seconds(self, cool_down_in_seconds):
        """
        Sets the cool_down_in_seconds of this AutoScalingPolicy.
        For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions.
        The cooldown period gives the system time to stabilize before rescaling. The minimum value is 600 seconds, which
        is also the default. The cooldown period starts when the model deployment becomes ACTIVE after the scaling operation.


        :param cool_down_in_seconds: The cool_down_in_seconds of this AutoScalingPolicy.
        :type: int
        """
        self._cool_down_in_seconds = cool_down_in_seconds

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this AutoScalingPolicy.
        Whether the autoscaling policy is enabled.


        :return: The is_enabled of this AutoScalingPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AutoScalingPolicy.
        Whether the autoscaling policy is enabled.


        :param is_enabled: The is_enabled of this AutoScalingPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def auto_scaling_policies(self):
        """
        **[Required]** Gets the auto_scaling_policies of this AutoScalingPolicy.
        The list of autoscaling policy details.


        :return: The auto_scaling_policies of this AutoScalingPolicy.
        :rtype: list[oci.data_science.models.AutoScalingPolicyDetails]
        """
        return self._auto_scaling_policies

    @auto_scaling_policies.setter
    def auto_scaling_policies(self, auto_scaling_policies):
        """
        Sets the auto_scaling_policies of this AutoScalingPolicy.
        The list of autoscaling policy details.


        :param auto_scaling_policies: The auto_scaling_policies of this AutoScalingPolicy.
        :type: list[oci.data_science.models.AutoScalingPolicyDetails]
        """
        self._auto_scaling_policies = auto_scaling_policies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
