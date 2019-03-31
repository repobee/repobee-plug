"""Utility classes and functions for repobee-plug.

.. module:: util
    :synopsis: Utility classes and functions for repobee-plug.

.. moduleauthor:: Simon Larsén
"""
import collections
import enum
import pluggy

hookspec = pluggy.HookspecMarker(__package__)
hookimpl = pluggy.HookimplMarker(__package__)

HookResult = collections.namedtuple('HookResult', ('hook', 'status', 'msg'))


class Status(enum.Enum):
    """Status codes enum."""
    SUCCESS = 'success'
    WARNING = 'warning'
    ERROR = 'error'
