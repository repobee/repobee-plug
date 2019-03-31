"""Exceptions for repomate_plug.

.. module:: exception
    :synopsis: Exceptions for repomate_plug.

.. moduleauthor:: Simon Larsén
"""


class PlugError(Exception):
    """Base class for all repomate_plug exceptions."""


class HookNameError(PlugError):
    """Raise when a public method in a class that inherits from
    :py:class:`~repomate_plug.Plugin` does not have a hook name.
    """
