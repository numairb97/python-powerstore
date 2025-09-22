# Copyright: (c) 2024, Dell Technologies

"""Input validation utilities for PowerStore"""

import re
from typing import Any, Dict, Union


def validate_string_input(value: Any, field_name: str, max_length: int = 255,
                          allow_empty: bool = False,
                          pattern: Union[str, None] = None) -> str:
    """Validate string input parameters

    :param value: The value to validate
    :param field_name: Name of the field for error messages
    :param max_length: Maximum allowed length
    :param allow_empty: Whether empty strings are allowed
    :param pattern: Optional regex pattern to match
    :return: Validated string value
    :raises ValueError: If validation fails
    """
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")

    if not allow_empty and not value.strip():
        raise ValueError(f"{field_name} cannot be empty")

    if len(value) > max_length:
        raise ValueError(f"{field_name} cannot exceed {max_length} characters")

    if pattern and not re.match(pattern, value):
        raise ValueError(f"{field_name} format is invalid")

    return value.strip()


def validate_id_parameter(value: Any, field_name: str) -> str:
    """Validate ID parameters (UUIDs, resource IDs, etc.)"""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")

    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty")

    if not re.match(r'^[a-zA-Z0-9\-_]+$', value):
        raise ValueError(f"{field_name} contains invalid characters")

    return value.strip()


def sanitize_query_parameters(params: Dict[str, Any]) -> Dict[str, Any]:
    """Sanitize query parameters to prevent injection attacks"""
    sanitized = {}
    for key, value in params.items():
        if isinstance(value, str):
            sanitized[key] = re.sub(r'[<>"\';]', '', value)
        else:
            sanitized[key] = value
    return sanitized
