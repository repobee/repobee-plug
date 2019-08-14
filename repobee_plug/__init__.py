import pluggy

from repobee_plug.__version import __version__
from repobee_plug.pluginmeta import Plugin
from repobee_plug.containers import hookimpl as repobee_hook
from repobee_plug.containers import HookResult
from repobee_plug.containers import Status
from repobee_plug.containers import ExtensionParser
from repobee_plug.containers import ExtensionCommand
from repobee_plug.containers import ReviewAllocation
from repobee_plug.corehooks import PeerReviewHook as _peer_hook
from repobee_plug.corehooks import APIHook as _api_hook
from repobee_plug.exthooks import CloneHook as _clone_hook
from repobee_plug.exthooks import ExtensionCommandHook as _ext_command_hook
from repobee_plug.serialize import json_to_result_mapping, result_mapping_to_json

from repobee_plug.apimeta import Team, TeamPermission, Issue, IssueState, Repo, API
from repobee_plug.exception import ExtensionCommandError, HookNameError, PlugError

manager = pluggy.PluginManager(__package__)
manager.add_hookspecs(_clone_hook)
manager.add_hookspecs(_peer_hook)
manager.add_hookspecs(_api_hook)
manager.add_hookspecs(_ext_command_hook)

__all__ = [
    "Plugin",
    "manager",
    "repobee_hook",
    "HookResult",
    "Status",
    "ExtensionParser",
    "ExtensionCommand",
    "ReviewAllocation",
    "Team",
    "TeamPermission",
    "Issue",
    "Repo",
    "Issue",
    "IssueState",
    "API",
    "ExtensionCommandError",
    "HookNameError",
    "PlugError",
    "json_to_result_mapping",
    "result_mapping_to_json",
]
