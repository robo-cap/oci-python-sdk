# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricBasedVerticalScaleUpConfig(object):
    """
    Configration for a metric based vertical scale-up policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MetricBasedVerticalScaleUpConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric:
            The value to assign to the metric property of this MetricBasedVerticalScaleUpConfig.
        :type metric: oci.bds.models.AutoScalePolicyMetricRule

        :param max_ocpus_per_node:
            The value to assign to the max_ocpus_per_node property of this MetricBasedVerticalScaleUpConfig.
        :type max_ocpus_per_node: int

        :param max_memory_per_node:
            The value to assign to the max_memory_per_node property of this MetricBasedVerticalScaleUpConfig.
        :type max_memory_per_node: int

        :param ocpu_step_size:
            The value to assign to the ocpu_step_size property of this MetricBasedVerticalScaleUpConfig.
        :type ocpu_step_size: int

        :param memory_step_size:
            The value to assign to the memory_step_size property of this MetricBasedVerticalScaleUpConfig.
        :type memory_step_size: int

        """
        self.swagger_types = {
            'metric': 'AutoScalePolicyMetricRule',
            'max_ocpus_per_node': 'int',
            'max_memory_per_node': 'int',
            'ocpu_step_size': 'int',
            'memory_step_size': 'int'
        }
        self.attribute_map = {
            'metric': 'metric',
            'max_ocpus_per_node': 'maxOcpusPerNode',
            'max_memory_per_node': 'maxMemoryPerNode',
            'ocpu_step_size': 'ocpuStepSize',
            'memory_step_size': 'memoryStepSize'
        }
        self._metric = None
        self._max_ocpus_per_node = None
        self._max_memory_per_node = None
        self._ocpu_step_size = None
        self._memory_step_size = None

    @property
    def metric(self):
        """
        Gets the metric of this MetricBasedVerticalScaleUpConfig.

        :return: The metric of this MetricBasedVerticalScaleUpConfig.
        :rtype: oci.bds.models.AutoScalePolicyMetricRule
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this MetricBasedVerticalScaleUpConfig.

        :param metric: The metric of this MetricBasedVerticalScaleUpConfig.
        :type: oci.bds.models.AutoScalePolicyMetricRule
        """
        self._metric = metric

    @property
    def max_ocpus_per_node(self):
        """
        Gets the max_ocpus_per_node of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the maximum number of OCPUs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :return: The max_ocpus_per_node of this MetricBasedVerticalScaleUpConfig.
        :rtype: int
        """
        return self._max_ocpus_per_node

    @max_ocpus_per_node.setter
    def max_ocpus_per_node(self, max_ocpus_per_node):
        """
        Sets the max_ocpus_per_node of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the maximum number of OCPUs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :param max_ocpus_per_node: The max_ocpus_per_node of this MetricBasedVerticalScaleUpConfig.
        :type: int
        """
        self._max_ocpus_per_node = max_ocpus_per_node

    @property
    def max_memory_per_node(self):
        """
        Gets the max_memory_per_node of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the maximum memory in GBs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :return: The max_memory_per_node of this MetricBasedVerticalScaleUpConfig.
        :rtype: int
        """
        return self._max_memory_per_node

    @max_memory_per_node.setter
    def max_memory_per_node(self, max_memory_per_node):
        """
        Sets the max_memory_per_node of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the maximum memory in GBs each node can be scaled-up to. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :param max_memory_per_node: The max_memory_per_node of this MetricBasedVerticalScaleUpConfig.
        :type: int
        """
        self._max_memory_per_node = max_memory_per_node

    @property
    def ocpu_step_size(self):
        """
        Gets the ocpu_step_size of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the number of OCPUs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :return: The ocpu_step_size of this MetricBasedVerticalScaleUpConfig.
        :rtype: int
        """
        return self._ocpu_step_size

    @ocpu_step_size.setter
    def ocpu_step_size(self, ocpu_step_size):
        """
        Sets the ocpu_step_size of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the number of OCPUs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :param ocpu_step_size: The ocpu_step_size of this MetricBasedVerticalScaleUpConfig.
        :type: int
        """
        self._ocpu_step_size = ocpu_step_size

    @property
    def memory_step_size(self):
        """
        Gets the memory_step_size of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the size of memory in GBs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :return: The memory_step_size of this MetricBasedVerticalScaleUpConfig.
        :rtype: int
        """
        return self._memory_step_size

    @memory_step_size.setter
    def memory_step_size(self, memory_step_size):
        """
        Sets the memory_step_size of this MetricBasedVerticalScaleUpConfig.
        For nodes with `flexible compute shapes`__, this value is the size of memory in GBs to add to each node during a scale-up event. This value is not used for nodes with fixed compute shapes.

        __ https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-shape


        :param memory_step_size: The memory_step_size of this MetricBasedVerticalScaleUpConfig.
        :type: int
        """
        self._memory_step_size = memory_step_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
