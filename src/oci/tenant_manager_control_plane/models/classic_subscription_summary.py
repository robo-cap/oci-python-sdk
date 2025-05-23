# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230401

from .subscription_summary import SubscriptionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClassicSubscriptionSummary(SubscriptionSummary):
    """
    Summary of subscription.
    """

    #: A constant which can be used with the lifecycle_state property of a ClassicSubscriptionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ClassicSubscriptionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ClassicSubscriptionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ClassicSubscriptionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ClassicSubscriptionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ClassicSubscriptionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ClassicSubscriptionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ClassicSubscriptionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.tenant_manager_control_plane.models.ClassicSubscriptionSummary.entity_version` attribute
        of this class is ``V1`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_version:
            The value to assign to the entity_version property of this ClassicSubscriptionSummary.
            Allowed values for this property are: "V1", "V2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_version: str

        :param id:
            The value to assign to the id property of this ClassicSubscriptionSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ClassicSubscriptionSummary.
        :type compartment_id: str

        :param service_name:
            The value to assign to the service_name property of this ClassicSubscriptionSummary.
        :type service_name: str

        :param time_created:
            The value to assign to the time_created property of this ClassicSubscriptionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ClassicSubscriptionSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ClassicSubscriptionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ClassicSubscriptionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ClassicSubscriptionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param classic_subscription_id:
            The value to assign to the classic_subscription_id property of this ClassicSubscriptionSummary.
        :type classic_subscription_id: str

        :param is_classic_subscription:
            The value to assign to the is_classic_subscription property of this ClassicSubscriptionSummary.
        :type is_classic_subscription: bool

        :param payment_model:
            The value to assign to the payment_model property of this ClassicSubscriptionSummary.
        :type payment_model: str

        :param region_assignment:
            The value to assign to the region_assignment property of this ClassicSubscriptionSummary.
        :type region_assignment: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ClassicSubscriptionSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param start_date:
            The value to assign to the start_date property of this ClassicSubscriptionSummary.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this ClassicSubscriptionSummary.
        :type end_date: datetime

        """
        self.swagger_types = {
            'entity_version': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'service_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'classic_subscription_id': 'str',
            'is_classic_subscription': 'bool',
            'payment_model': 'str',
            'region_assignment': 'str',
            'lifecycle_state': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime'
        }
        self.attribute_map = {
            'entity_version': 'entityVersion',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'service_name': 'serviceName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'classic_subscription_id': 'classicSubscriptionId',
            'is_classic_subscription': 'isClassicSubscription',
            'payment_model': 'paymentModel',
            'region_assignment': 'regionAssignment',
            'lifecycle_state': 'lifecycleState',
            'start_date': 'startDate',
            'end_date': 'endDate'
        }
        self._entity_version = None
        self._id = None
        self._compartment_id = None
        self._service_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._classic_subscription_id = None
        self._is_classic_subscription = None
        self._payment_model = None
        self._region_assignment = None
        self._lifecycle_state = None
        self._start_date = None
        self._end_date = None
        self._entity_version = 'V1'

    @property
    def classic_subscription_id(self):
        """
        **[Required]** Gets the classic_subscription_id of this ClassicSubscriptionSummary.
        Classic subscription ID.


        :return: The classic_subscription_id of this ClassicSubscriptionSummary.
        :rtype: str
        """
        return self._classic_subscription_id

    @classic_subscription_id.setter
    def classic_subscription_id(self, classic_subscription_id):
        """
        Sets the classic_subscription_id of this ClassicSubscriptionSummary.
        Classic subscription ID.


        :param classic_subscription_id: The classic_subscription_id of this ClassicSubscriptionSummary.
        :type: str
        """
        self._classic_subscription_id = classic_subscription_id

    @property
    def is_classic_subscription(self):
        """
        Gets the is_classic_subscription of this ClassicSubscriptionSummary.
        Specifies whether or not the subscription is from classic systems.


        :return: The is_classic_subscription of this ClassicSubscriptionSummary.
        :rtype: bool
        """
        return self._is_classic_subscription

    @is_classic_subscription.setter
    def is_classic_subscription(self, is_classic_subscription):
        """
        Sets the is_classic_subscription of this ClassicSubscriptionSummary.
        Specifies whether or not the subscription is from classic systems.


        :param is_classic_subscription: The is_classic_subscription of this ClassicSubscriptionSummary.
        :type: bool
        """
        self._is_classic_subscription = is_classic_subscription

    @property
    def payment_model(self):
        """
        Gets the payment_model of this ClassicSubscriptionSummary.
        The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.


        :return: The payment_model of this ClassicSubscriptionSummary.
        :rtype: str
        """
        return self._payment_model

    @payment_model.setter
    def payment_model(self, payment_model):
        """
        Sets the payment_model of this ClassicSubscriptionSummary.
        The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.


        :param payment_model: The payment_model of this ClassicSubscriptionSummary.
        :type: str
        """
        self._payment_model = payment_model

    @property
    def region_assignment(self):
        """
        Gets the region_assignment of this ClassicSubscriptionSummary.
        Region for the subscription.


        :return: The region_assignment of this ClassicSubscriptionSummary.
        :rtype: str
        """
        return self._region_assignment

    @region_assignment.setter
    def region_assignment(self, region_assignment):
        """
        Sets the region_assignment of this ClassicSubscriptionSummary.
        Region for the subscription.


        :param region_assignment: The region_assignment of this ClassicSubscriptionSummary.
        :type: str
        """
        self._region_assignment = region_assignment

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ClassicSubscriptionSummary.
        Lifecycle state of the subscription.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ClassicSubscriptionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ClassicSubscriptionSummary.
        Lifecycle state of the subscription.


        :param lifecycle_state: The lifecycle_state of this ClassicSubscriptionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def start_date(self):
        """
        Gets the start_date of this ClassicSubscriptionSummary.
        Subscription start time.


        :return: The start_date of this ClassicSubscriptionSummary.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ClassicSubscriptionSummary.
        Subscription start time.


        :param start_date: The start_date of this ClassicSubscriptionSummary.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this ClassicSubscriptionSummary.
        Subscription end time.


        :return: The end_date of this ClassicSubscriptionSummary.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ClassicSubscriptionSummary.
        Subscription end time.


        :param end_date: The end_date of this ClassicSubscriptionSummary.
        :type: datetime
        """
        self._end_date = end_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
