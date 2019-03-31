"""Hookspecs for repobee extension hooks.

Extension hooks add something to the functionality of repobee, but are not
necessary for its operation. Currently, all extension hooks are related to
cloning repos.

.. module:: exthooks
    :synopsis: Hookspecs for repobee extension hooks.

.. moduleauthor:: Simon Larsén
"""

import pathlib
import argparse
import configparser
from typing import Union, Optional

from repobee_plug.util import hookspec
from repobee_plug.util import HookResult


class CloneHook:
    """Hook functions related to cloning repos."""

    @hookspec
    def act_on_cloned_repo(self, path: Union[str, pathlib.Path],
                           api) -> Optional[HookResult]:
        """Do something with a cloned repo.

        Args:
            path: Path to the repo.
            api: An instance of :py:class:`repobee.github_api.GitHubAPI`.

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
