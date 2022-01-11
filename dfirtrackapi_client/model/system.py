"""
    DFIRTrack

    OpenAPI 3 - Documentation of DFIRTrack API  # noqa: E501

    The version of the OpenAPI document: v2.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from dfirtrackapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from dfirtrackapi_client.exceptions import ApiAttributeError



class System(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('system_name',): {
            'max_length': 50,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'system_name': (str,),  # noqa: E501
            'systemstatus': (int,),  # noqa: E501
            'system_created_by_user_id': (int,),  # noqa: E501
            'system_modified_by_user_id': (int,),  # noqa: E501
            'system_id': (int,),  # noqa: E501
            'system_uuid': (str,),  # noqa: E501
            'domain': (int, none_type,),  # noqa: E501
            'dnsname': (int, none_type,),  # noqa: E501
            'analysisstatus': (int, none_type,),  # noqa: E501
            'reason': (int, none_type,),  # noqa: E501
            'recommendation': (int, none_type,),  # noqa: E501
            'systemtype': (int, none_type,),  # noqa: E501
            'ip': ([int],),  # noqa: E501
            'os': (int, none_type,),  # noqa: E501
            'osarch': (int, none_type,),  # noqa: E501
            'system_lastbooted_time': (datetime, none_type,),  # noqa: E501
            'system_deprecated_time': (datetime, none_type,),  # noqa: E501
            'system_is_vm': (bool, none_type,),  # noqa: E501
            'host_system': (int, none_type,),  # noqa: E501
            'company': ([int],),  # noqa: E501
            'location': (int, none_type,),  # noqa: E501
            'serviceprovider': (int, none_type,),  # noqa: E501
            'contact': (int, none_type,),  # noqa: E501
            'tag': ([int],),  # noqa: E501
            'case': ([int],),  # noqa: E501
            'system_create_time': (datetime,),  # noqa: E501
            'system_modify_time': (datetime,),  # noqa: E501
            'system_export_markdown': (bool,),  # noqa: E501
            'system_export_spreadsheet': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'system_name': 'system_name',  # noqa: E501
        'systemstatus': 'systemstatus',  # noqa: E501
        'system_created_by_user_id': 'system_created_by_user_id',  # noqa: E501
        'system_modified_by_user_id': 'system_modified_by_user_id',  # noqa: E501
        'system_id': 'system_id',  # noqa: E501
        'system_uuid': 'system_uuid',  # noqa: E501
        'domain': 'domain',  # noqa: E501
        'dnsname': 'dnsname',  # noqa: E501
        'analysisstatus': 'analysisstatus',  # noqa: E501
        'reason': 'reason',  # noqa: E501
        'recommendation': 'recommendation',  # noqa: E501
        'systemtype': 'systemtype',  # noqa: E501
        'ip': 'ip',  # noqa: E501
        'os': 'os',  # noqa: E501
        'osarch': 'osarch',  # noqa: E501
        'system_lastbooted_time': 'system_lastbooted_time',  # noqa: E501
        'system_deprecated_time': 'system_deprecated_time',  # noqa: E501
        'system_is_vm': 'system_is_vm',  # noqa: E501
        'host_system': 'host_system',  # noqa: E501
        'company': 'company',  # noqa: E501
        'location': 'location',  # noqa: E501
        'serviceprovider': 'serviceprovider',  # noqa: E501
        'contact': 'contact',  # noqa: E501
        'tag': 'tag',  # noqa: E501
        'case': 'case',  # noqa: E501
        'system_create_time': 'system_create_time',  # noqa: E501
        'system_modify_time': 'system_modify_time',  # noqa: E501
        'system_export_markdown': 'system_export_markdown',  # noqa: E501
        'system_export_spreadsheet': 'system_export_spreadsheet',  # noqa: E501
    }

    read_only_vars = {
        'system_id',  # noqa: E501
        'system_uuid',  # noqa: E501
        'system_create_time',  # noqa: E501
        'system_modify_time',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, system_name, systemstatus, system_created_by_user_id, system_modified_by_user_id, *args, **kwargs):  # noqa: E501
        """System - a model defined in OpenAPI

        Args:
            system_name (str):
            systemstatus (int):
            system_created_by_user_id (int):
            system_modified_by_user_id (int):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            system_id (int): [optional]  # noqa: E501
            system_uuid (str): [optional]  # noqa: E501
            domain (int, none_type): [optional]  # noqa: E501
            dnsname (int, none_type): [optional]  # noqa: E501
            analysisstatus (int, none_type): [optional]  # noqa: E501
            reason (int, none_type): [optional]  # noqa: E501
            recommendation (int, none_type): [optional]  # noqa: E501
            systemtype (int, none_type): [optional]  # noqa: E501
            ip ([int]): [optional]  # noqa: E501
            os (int, none_type): [optional]  # noqa: E501
            osarch (int, none_type): [optional]  # noqa: E501
            system_lastbooted_time (datetime, none_type): [optional]  # noqa: E501
            system_deprecated_time (datetime, none_type): [optional]  # noqa: E501
            system_is_vm (bool, none_type): [optional]  # noqa: E501
            host_system (int, none_type): [optional]  # noqa: E501
            company ([int]): [optional]  # noqa: E501
            location (int, none_type): [optional]  # noqa: E501
            serviceprovider (int, none_type): [optional]  # noqa: E501
            contact (int, none_type): [optional]  # noqa: E501
            tag ([int]): [optional]  # noqa: E501
            case ([int]): [optional]  # noqa: E501
            system_create_time (datetime): [optional]  # noqa: E501
            system_modify_time (datetime): [optional]  # noqa: E501
            system_export_markdown (bool): [optional]  # noqa: E501
            system_export_spreadsheet (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.system_name = system_name
        self.systemstatus = systemstatus
        self.system_created_by_user_id = system_created_by_user_id
        self.system_modified_by_user_id = system_modified_by_user_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, system_name, systemstatus, system_created_by_user_id, system_modified_by_user_id, *args, **kwargs):  # noqa: E501
        """System - a model defined in OpenAPI

        Args:
            system_name (str):
            systemstatus (int):
            system_created_by_user_id (int):
            system_modified_by_user_id (int):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            system_id (int): [optional]  # noqa: E501
            system_uuid (str): [optional]  # noqa: E501
            domain (int, none_type): [optional]  # noqa: E501
            dnsname (int, none_type): [optional]  # noqa: E501
            analysisstatus (int, none_type): [optional]  # noqa: E501
            reason (int, none_type): [optional]  # noqa: E501
            recommendation (int, none_type): [optional]  # noqa: E501
            systemtype (int, none_type): [optional]  # noqa: E501
            ip ([int]): [optional]  # noqa: E501
            os (int, none_type): [optional]  # noqa: E501
            osarch (int, none_type): [optional]  # noqa: E501
            system_lastbooted_time (datetime, none_type): [optional]  # noqa: E501
            system_deprecated_time (datetime, none_type): [optional]  # noqa: E501
            system_is_vm (bool, none_type): [optional]  # noqa: E501
            host_system (int, none_type): [optional]  # noqa: E501
            company ([int]): [optional]  # noqa: E501
            location (int, none_type): [optional]  # noqa: E501
            serviceprovider (int, none_type): [optional]  # noqa: E501
            contact (int, none_type): [optional]  # noqa: E501
            tag ([int]): [optional]  # noqa: E501
            case ([int]): [optional]  # noqa: E501
            system_create_time (datetime): [optional]  # noqa: E501
            system_modify_time (datetime): [optional]  # noqa: E501
            system_export_markdown (bool): [optional]  # noqa: E501
            system_export_spreadsheet (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.system_name = system_name
        self.systemstatus = systemstatus
        self.system_created_by_user_id = system_created_by_user_id
        self.system_modified_by_user_id = system_modified_by_user_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
