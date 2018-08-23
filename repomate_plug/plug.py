"""Hook specifications.

.. module:: hookspec
    :synopsis: Hook specifications.

.. moduleauthor:: Simon Larsén
"""
import pathlib
import argparse
import configparser
import collections
from typing import Union, Optional

import pluggy

hookspec = pluggy.HookspecMarker(__package__)
hookimpl = pluggy.HookimplMarker(__package__)

pm = pluggy.PluginManager(__package__)

HookResult = collections.namedtuple('HookResult', ('hook', 'status', 'msg'))

# status messages
ERROR = "error"
WARNING = "warning"
SUCCESS = "success"


class Plugin:
    """Wrapper class for plugin classes. Used to dynamically detect plugin
    classes during plugin registration. Any plugin class must be decorated
    with this class.
    """

    def __init__(self, class_):
        assert isinstance(class_, type)  # sanity check
        self._class = class_

    def __call__(self, *args, **kwargs):
        return self._class(*args, **kwargs)


class CloneHook:
    """Hook functions related to cloning repos."""

    @hookspec
    def act_on_cloned_repo(
            self, path: Union[str, pathlib.Path]) -> Optional[HookResult]:
        """Do something with a cloned repo.

        Args:
            path: Path to the repo.

        Returns:
            optionally returns a HookResult namedtuple for reporting the
            outcome of the hook. May also return None, in which case no
            reporting will be performed for the hook.
        """

    @hookspec
    def clone_parser_hook(self, clone_parser: argparse.ArgumentParser) -> None:
        """Do something with the clone repos subparser before it is used used to
        parse CLI options. The typical task is to add options to it.

        Args:
            clone_parser: The ``clone`` subparser.
        """

    @hookspec
    def parse_args(self, args: argparse.Namespace) -> None:
        """Get the raw args from the parser. Only called for the clone parser.
        The typical task is to fetch any values from options added in
        :py:func:`clone_parser_hook`.

        Args:
            args: The full namespace returned by
            :py:func:`argparse.ArgumentParser.parse_args`
        """

    @hookspec
    def config_hook(self, config_parser: configparser.ConfigParser) -> None:
        """Hook into the config file parsing.
        
        Args:
            config: the config parser after config has been read.
        """


pm.add_hookspecs(CloneHook)
