"""Task data structure and related functionality.

.. module:: tasks
    :synopsis: Task data structure and related functionality.

.. moduleauthor:: Simon Larsén
"""
import pathlib
import collections
from typing import Callable, Optional

from repobee_plug import exception
from repobee_plug import apimeta
from repobee_plug import containers


class Task(
    collections.namedtuple(
        "Task", ("act", "add_option", "handle_args", "handle_config", "persist_changes")
    )
):
    """A data structure for describing a task. Tasks are operations that
    plugins can define to run on for example cloned student repos (a clone
    task) or on master repos before setting up student repos (a setup task).

    Attributes:
        act: A callback function that takes the path to a repository worktree
            and an API instance, and optionally returns a HookResult to report
            results.
        add_option: A callback function that adds options to the CLI parser.
        handle_args: A callback function that receives the parsed CLI args.
        handle_config: A callback function that receives the config parser.
        persist_changes (bool): If True, the task requires that changes to the
            repository that has been acted upon be persisted. This means
            different things in different contexts (e.g.  whether the task is
            executed in a clone context or in a setup context), and may not be
            supported for all contexts.

    The callback methods should have the following headers.

    .. code-block:: python

        def act(path: pathlib.Path, api: plug.API) -> Optional[containers.HookResult]:

        def add_option(parser: argparse.ArgumentParser) -> None:

        def handle_args(args: argparse.Namespace) -> None:

        def handle_config(config_parser: configparser.ConfigParser) -> None:

    .. important::

        The ``act`` callback should *never* change the Git repository it acts
        upon (e.g. running commands such as ``git add``, ``git checkout`` or
        ``git commit``). This can have adverse and unexpected effects on
        RepoBee's functionality. It is however free to change the working tree
        however it wants.

    Each callback is called at most once. They are not guaranteed to execute,
    because there may be an unexpected crash somewhere else, or the plugin may
    not come into scope (for example, a clone task plugin will not come into
    scope if ``repobee setup`` is run). The callbacks can do whatever is
    appropriate for the plugin, except for changing any Git repositories. For
    information on the types used in the callbacks, see the Python stdlib
    documentation for :py:mod:`argparse` and :py:mod:`configparser`.
    """

    def __new__(
        cls,
        act,
        add_option=None,
        handle_args=None,
        handle_config=None,
        persist_changes=False,
    ):
        return super().__new__(
            cls, act, add_option, handle_args, handle_config, persist_changes
        )
