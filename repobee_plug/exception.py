"""Exceptions for repobee_plug.

.. module:: exception
    :synopsis: Exceptions for repobee_plug.

.. moduleauthor:: Simon Larsén
"""


class PlugError(Exception):
    """Base class for all repobee_plug exceptions."""


class HookNameError(PlugError):
    """Raise when a public method in a class that inherits from
    :py:class:`~repobee_plug.Plugin` does not have a hook name.
    """


class ExtensionCommandError(PlugError):
    """Raise when an :py:class:~repobee_plug.containers.ExtensionCommand: is
    incorrectly defined.
    """
