"""Constants file."""

from enum import Enum


class ResponseConstants(Enum):
    """Constants for response."""

    ERROR_KEY = 'error'
    STATUS_KEY = 'status'
    STATUS_SUCCESS = 'Success'
    STATUS_ERROR = 'Error'
    DATA_KEY = 'data'
