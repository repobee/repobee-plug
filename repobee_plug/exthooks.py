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

from repobee_plug.containers import hookspec
from repobee_plug.containers import HookResult
from repobee_plug.containers import ExtensionCommand


class CloneHook:
    """Hook functions related to cloning repos."""

    @hookspec
    def act_on_cloned_repo(
        self, path: Union[str, pathlib.Path], api
    ) -> Optional[HookResult]:
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


class ExtensionCommandHook:
    """Hooks related to extension commands."""

    @hookspec
    def create_extension_command(self) -> ExtensionCommand:
        """Create an extension command to add to the RepoBee CLI. The command will
        be added as one of the top-level subcommands of RepoBee. It should return
        an :py:class:`~repobee_plug.containers.ExtensionCommand`.

        .. code-block:: python
            
            def command(args: argparse.Namespace, api: apimeta.API)

        The ``command`` function will be called if the extension command is used
        on the command line.

        Note that the :py:class:`~repobee_plug.containers.RepoBeeExtensionParser` class
        is just a thin wrapper around :py:class:`argparse.ArgumentParser`, and can
        be used in an identical manner. The following is an example definition
        of this hook that adds a subcommand called ``example-command``, that can
        be called with ``repobee example-command``.

        .. code-block:: python

            def callback(args: argparse.Namespace, api: apimeta.API) -> None:
                LOGGER.info("callback called with: {}, {}".format(args, api))

            @plug.repobee_hook
            def create_extension_command():
                parser = plug.RepoBeeExtensionParser()
                parser.add_argument("-b", "--bb", help="A useless argument")
                return plug.ExtensionCommand(
                    parser=parser,
                    name="example-command",
                    help="An example command",
                    description="Description of an example command",
                    callback=callback,
                )

        .. important:

            The ``-tb|--traceback`` argument is always added to the parser.
            Make sure not to add any conflicting arguments.

        .. important::

            If you need to use the api, you set ``requires_api=True`` in the
            ``ExtensionCommand``. This will automatically add the options that
            the API requires to the CLI options of the subcommand, and
            initialize the api and pass it in.

        Returns:
            A :py:class:`~repobee_plug.containers.ExtensionCommand`.
        """
