import pluggy

from repomate_plug.__version import __version__
from repomate_plug.pluginmeta import Plugin
from repomate_plug.util import hookimpl as repomate_hook
from repomate_plug.util import HookResult
from repomate_plug.util import Status
from repomate_plug.corehooks import PeerReviewHook as _peer_hook
from repomate_plug.exthooks import CloneHook as _clone_hook

manager = pluggy.PluginManager(__package__)
manager.add_hookspecs(_clone_hook)
manager.add_hookspecs(_peer_hook)

__all__ = ["Plugin", "manager", "repomate_hook", "HookResult", "Status"]
