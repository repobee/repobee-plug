import pluggy

from repobee_plug.__version import __version__
from repobee_plug.pluginmeta import Plugin
from repobee_plug.util import hookimpl as repobee_hook
from repobee_plug.util import HookResult
from repobee_plug.util import Status
from repobee_plug.corehooks import PeerReviewHook as _peer_hook
from repobee_plug.exthooks import CloneHook as _clone_hook

manager = pluggy.PluginManager(__package__)
manager.add_hookspecs(_clone_hook)
manager.add_hookspecs(_peer_hook)

__all__ = ["Plugin", "manager", "repobee_hook", "HookResult", "Status"]
