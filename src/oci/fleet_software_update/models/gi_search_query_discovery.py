# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528

from .gi_fleet_discovery_details import GiFleetDiscoveryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GiSearchQueryDiscovery(GiFleetDiscoveryDetails):
    """
    Collection discovery done from the results of the specified Search Service query string.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GiSearchQueryDiscovery object with values from keyword arguments. The default value of the :py:attr:`~oci.fleet_software_update.models.GiSearchQueryDiscovery.strategy` attribute
        of this class is ``SEARCH_QUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy:
            The value to assign to the strategy property of this GiSearchQueryDiscovery.
            Allowed values for this property are: "SEARCH_QUERY", "FILTERS", "TARGET_LIST", "DISCOVERY_RESULTS"
        :type strategy: str

        :param query:
            The value to assign to the query property of this GiSearchQueryDiscovery.
        :type query: str

        """
        self.swagger_types = {
            'strategy': 'str',
            'query': 'str'
        }
        self.attribute_map = {
            'strategy': 'strategy',
            'query': 'query'
        }
        self._strategy = None
        self._query = None
        self._strategy = 'SEARCH_QUERY'

    @property
    def query(self):
        """
        **[Required]** Gets the query of this GiSearchQueryDiscovery.
        OCI Search Service query string.


        :return: The query of this GiSearchQueryDiscovery.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this GiSearchQueryDiscovery.
        OCI Search Service query string.


        :param query: The query of this GiSearchQueryDiscovery.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
