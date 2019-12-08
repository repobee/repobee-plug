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


class Task(collections.namedtuple("Task", ("callback",))):
    """A data structure for describing a task. Tasks are operations that
    plugins can define to run on for example cloned student repos (a clone
    task) or on master repos before setting up student repos (a setup task).

    Attributes:
        callback: A callback method that takes the path to a repository worktree
        and an API instance, and optionally returns a HookResult to report
        results.

    The callback method should be on the following form (although type
    annotations and names are not enforced).

    .. code-block::python

        def callback(path: pathlib.Path, api: plug.API) -> Optional[plug.HookResult]:
    """
