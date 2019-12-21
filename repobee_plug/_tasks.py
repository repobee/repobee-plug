"""Task data structure and related functionality.

.. module:: tasks
    :synopsis: Task data structure and related functionality.

.. moduleauthor:: Simon Larsén
"""
import collections


class Task(
    collections.namedtuple(
        "Task",
        (
            "act",
            "add_option",
            "handle_args",
            "handle_config",
            "persist_changes",
        ),
    )
):
    """A data structure for describing a task. Tasks are operations that
    plugins can define to run on for example cloned student repos (a clone
    task) or on master repos before setting up student repos (a setup task).
    Only the ``act`` attribute is required, all other attributes can be
    omitted.

    Note that the types of the attributes below are written with arrow notation
    for functions on the following form:

    .. code-block:: python

        (arg_type_1, arg_type_2, ...) -> return_type

    Attributes:
        act ((pathlib.Path, API) -> Optional[HookResult]]): A required callback
            function that takes the path to a repository worktree and an API
            instance, and optionally returns a HookResult to report results.
        add_option (Optional[ (argparse.ArgumentParser) -> None ]): An optional
            callback function that adds options to the CLI parser.
        handle_args (Optional[ (argparse.Namespace) -> None ]): An optional
            callback function that receives the parsed CLI args.
        handle_config (Optional[ (configparser.ConfigParser) -> None ]): An
            optional callback function that receives the config parser.
        persist_changes (bool): If True, the task requires that changes to the
            repository that has been acted upon be persisted. This means
            different things in different contexts (e.g.  whether the task is
            executed in a clone context or in a setup context), and may not be
            supported for all contexts.

    The callback methods should have the following headers.

    .. code-block:: python

        def act(
            path: pathlib.Path, api: repobee_plug.API
        ) -> Optional[containers.HookResult]:

        def add_option(parser: argparse.ArgumentParser) -> None:

        def handle_args(args: argparse.Namespace) -> None:

        def handle_config(config_parser: configparser.ConfigParser) -> None:

    .. note::

        The functions are called in the following order: ``add_option`` ->
        ``handle_config`` -> ``handle_args`` -> ``act``.

    .. important::

        The ``act`` callback should *never* change the Git repository it acts
        upon (e.g. running commands such as ``git add``, ``git checkout`` or
        ``git commit``). This can have adverse and unexpected effects on
        RepoBee's functionality. It is however absolutely fine to change the
        files in the Git working tree, as long as nothing is added or
        committed.

    Each callback is called at most once. They are not guaranteed to execute,
    because there may be an unexpected crash somewhere else, or the plugin may
    not come into scope (for example, a clone task plugin will not come into
    scope if ``repobee setup`` is run). The callbacks can do whatever is
    appropriate for the plugin, except for changing any Git repositories. For
    information on the types used in the callbacks, see the Python stdlib
    documentation for :py:mod:`argparse` and :py:mod:`configparser`.

    As an example, a simple clone task can be defined like so:

    .. code-block:: python

        import repobee_plug as plug

        def act(path, api):
            return plug.HookResult(
                hook="example",
                msg="IT LIVES!",
                status=plug.Status.SUCCESS
            )

        @plug.repobee_hook
        def clone_task():
            return plug.Task(act=act)

    For more elaborate instructions on creating tasks, see the tutorial.
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

    def __init__(
        self,
        act,
        add_option=None,
        handle_args=None,
        handle_config=None,
        persist_changes=False,
    ):
        """This is just for documentation."""
        return super().__init__(
            act, add_option, handle_args, handle_config, persist_changes
        )
