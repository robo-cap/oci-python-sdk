# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AgentInstallerSummary(object):
    """
    Supported agent installer downloads.
    """

    #: A constant which can be used with the os_family property of a AgentInstallerSummary.
    #: This constant has a value of "LINUX"
    OS_FAMILY_LINUX = "LINUX"

    #: A constant which can be used with the os_family property of a AgentInstallerSummary.
    #: This constant has a value of "WINDOWS"
    OS_FAMILY_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_family property of a AgentInstallerSummary.
    #: This constant has a value of "MACOS"
    OS_FAMILY_MACOS = "MACOS"

    #: A constant which can be used with the os_family property of a AgentInstallerSummary.
    #: This constant has a value of "UNKNOWN"
    OS_FAMILY_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the platform_architecture property of a AgentInstallerSummary.
    #: This constant has a value of "X86_64"
    PLATFORM_ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the platform_architecture property of a AgentInstallerSummary.
    #: This constant has a value of "X86"
    PLATFORM_ARCHITECTURE_X86 = "X86"

    #: A constant which can be used with the platform_architecture property of a AgentInstallerSummary.
    #: This constant has a value of "AARCH64"
    PLATFORM_ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the package_type property of a AgentInstallerSummary.
    #: This constant has a value of "RPM"
    PACKAGE_TYPE_RPM = "RPM"

    #: A constant which can be used with the package_type property of a AgentInstallerSummary.
    #: This constant has a value of "ZIP"
    PACKAGE_TYPE_ZIP = "ZIP"

    def __init__(self, **kwargs):
        """
        Initializes a new AgentInstallerSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param agent_installer_id:
            The value to assign to the agent_installer_id property of this AgentInstallerSummary.
        :type agent_installer_id: int

        :param agent_installer_description:
            The value to assign to the agent_installer_description property of this AgentInstallerSummary.
        :type agent_installer_description: str

        :param approximate_file_size_in_bytes:
            The value to assign to the approximate_file_size_in_bytes property of this AgentInstallerSummary.
        :type approximate_file_size_in_bytes: int

        :param sha256:
            The value to assign to the sha256 property of this AgentInstallerSummary.
        :type sha256: str

        :param os_family:
            The value to assign to the os_family property of this AgentInstallerSummary.
            Allowed values for this property are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param platform_architecture:
            The value to assign to the platform_architecture property of this AgentInstallerSummary.
            Allowed values for this property are: "X86_64", "X86", "AARCH64", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_architecture: str

        :param package_type:
            The value to assign to the package_type property of this AgentInstallerSummary.
            Allowed values for this property are: "RPM", "ZIP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param agent_version:
            The value to assign to the agent_version property of this AgentInstallerSummary.
        :type agent_version: str

        :param java_version:
            The value to assign to the java_version property of this AgentInstallerSummary.
        :type java_version: str

        :param agent_installer_version:
            The value to assign to the agent_installer_version property of this AgentInstallerSummary.
        :type agent_installer_version: str

        """
        self.swagger_types = {
            'agent_installer_id': 'int',
            'agent_installer_description': 'str',
            'approximate_file_size_in_bytes': 'int',
            'sha256': 'str',
            'os_family': 'str',
            'platform_architecture': 'str',
            'package_type': 'str',
            'agent_version': 'str',
            'java_version': 'str',
            'agent_installer_version': 'str'
        }
        self.attribute_map = {
            'agent_installer_id': 'agentInstallerId',
            'agent_installer_description': 'agentInstallerDescription',
            'approximate_file_size_in_bytes': 'approximateFileSizeInBytes',
            'sha256': 'sha256',
            'os_family': 'osFamily',
            'platform_architecture': 'platformArchitecture',
            'package_type': 'packageType',
            'agent_version': 'agentVersion',
            'java_version': 'javaVersion',
            'agent_installer_version': 'agentInstallerVersion'
        }
        self._agent_installer_id = None
        self._agent_installer_description = None
        self._approximate_file_size_in_bytes = None
        self._sha256 = None
        self._os_family = None
        self._platform_architecture = None
        self._package_type = None
        self._agent_version = None
        self._java_version = None
        self._agent_installer_version = None

    @property
    def agent_installer_id(self):
        """
        **[Required]** Gets the agent_installer_id of this AgentInstallerSummary.
        Unique identifier for the agent installer.


        :return: The agent_installer_id of this AgentInstallerSummary.
        :rtype: int
        """
        return self._agent_installer_id

    @agent_installer_id.setter
    def agent_installer_id(self, agent_installer_id):
        """
        Sets the agent_installer_id of this AgentInstallerSummary.
        Unique identifier for the agent installer.


        :param agent_installer_id: The agent_installer_id of this AgentInstallerSummary.
        :type: int
        """
        self._agent_installer_id = agent_installer_id

    @property
    def agent_installer_description(self):
        """
        **[Required]** Gets the agent_installer_description of this AgentInstallerSummary.
        Description of the agent installer artifact. The description typically includes the OS, architecture, and agent installer type.


        :return: The agent_installer_description of this AgentInstallerSummary.
        :rtype: str
        """
        return self._agent_installer_description

    @agent_installer_description.setter
    def agent_installer_description(self, agent_installer_description):
        """
        Sets the agent_installer_description of this AgentInstallerSummary.
        Description of the agent installer artifact. The description typically includes the OS, architecture, and agent installer type.


        :param agent_installer_description: The agent_installer_description of this AgentInstallerSummary.
        :type: str
        """
        self._agent_installer_description = agent_installer_description

    @property
    def approximate_file_size_in_bytes(self):
        """
        **[Required]** Gets the approximate_file_size_in_bytes of this AgentInstallerSummary.
        Approximate compressed file size in bytes.


        :return: The approximate_file_size_in_bytes of this AgentInstallerSummary.
        :rtype: int
        """
        return self._approximate_file_size_in_bytes

    @approximate_file_size_in_bytes.setter
    def approximate_file_size_in_bytes(self, approximate_file_size_in_bytes):
        """
        Sets the approximate_file_size_in_bytes of this AgentInstallerSummary.
        Approximate compressed file size in bytes.


        :param approximate_file_size_in_bytes: The approximate_file_size_in_bytes of this AgentInstallerSummary.
        :type: int
        """
        self._approximate_file_size_in_bytes = approximate_file_size_in_bytes

    @property
    def sha256(self):
        """
        **[Required]** Gets the sha256 of this AgentInstallerSummary.
        SHA256 checksum of the agent installer.


        :return: The sha256 of this AgentInstallerSummary.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """
        Sets the sha256 of this AgentInstallerSummary.
        SHA256 checksum of the agent installer.


        :param sha256: The sha256 of this AgentInstallerSummary.
        :type: str
        """
        self._sha256 = sha256

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this AgentInstallerSummary.
        The target operating system family for the agent installer.

        Allowed values for this property are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this AgentInstallerSummary.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this AgentInstallerSummary.
        The target operating system family for the agent installer.


        :param os_family: The os_family of this AgentInstallerSummary.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def platform_architecture(self):
        """
        **[Required]** Gets the platform_architecture of this AgentInstallerSummary.
        The target operating system architecture for the installer.

        Allowed values for this property are: "X86_64", "X86", "AARCH64", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_architecture of this AgentInstallerSummary.
        :rtype: str
        """
        return self._platform_architecture

    @platform_architecture.setter
    def platform_architecture(self, platform_architecture):
        """
        Sets the platform_architecture of this AgentInstallerSummary.
        The target operating system architecture for the installer.


        :param platform_architecture: The platform_architecture of this AgentInstallerSummary.
        :type: str
        """
        allowed_values = ["X86_64", "X86", "AARCH64"]
        if not value_allowed_none_or_none_sentinel(platform_architecture, allowed_values):
            platform_architecture = 'UNKNOWN_ENUM_VALUE'
        self._platform_architecture = platform_architecture

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this AgentInstallerSummary.
        The package type (typically the file extension) of the agent software included in the installer.

        Allowed values for this property are: "RPM", "ZIP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this AgentInstallerSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this AgentInstallerSummary.
        The package type (typically the file extension) of the agent software included in the installer.


        :param package_type: The package_type of this AgentInstallerSummary.
        :type: str
        """
        allowed_values = ["RPM", "ZIP"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def agent_version(self):
        """
        **[Required]** Gets the agent_version of this AgentInstallerSummary.
        Agent image version.


        :return: The agent_version of this AgentInstallerSummary.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """
        Sets the agent_version of this AgentInstallerSummary.
        Agent image version.


        :param agent_version: The agent_version of this AgentInstallerSummary.
        :type: str
        """
        self._agent_version = agent_version

    @property
    def java_version(self):
        """
        **[Required]** Gets the java_version of this AgentInstallerSummary.
        Java version.


        :return: The java_version of this AgentInstallerSummary.
        :rtype: str
        """
        return self._java_version

    @java_version.setter
    def java_version(self, java_version):
        """
        Sets the java_version of this AgentInstallerSummary.
        Java version.


        :param java_version: The java_version of this AgentInstallerSummary.
        :type: str
        """
        self._java_version = java_version

    @property
    def agent_installer_version(self):
        """
        **[Required]** Gets the agent_installer_version of this AgentInstallerSummary.
        Agent installer version.


        :return: The agent_installer_version of this AgentInstallerSummary.
        :rtype: str
        """
        return self._agent_installer_version

    @agent_installer_version.setter
    def agent_installer_version(self, agent_installer_version):
        """
        Sets the agent_installer_version of this AgentInstallerSummary.
        Agent installer version.


        :param agent_installer_version: The agent_installer_version of this AgentInstallerSummary.
        :type: str
        """
        self._agent_installer_version = agent_installer_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
