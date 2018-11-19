Plugin system overview
**********************

Conventions
===========
For ``repomate`` to discover a plugin and its hooks, the following conventions
need to be adhered to:

1. The PyPi package should be named ``repomate-<plugin>``, where ``<plugin>``
   is the name of the plugin.
2. The actual Python package (i.e. the directory in which the source files
   are located) should be called ``repomate_<plugin>``. In other words,
   replace the hyphen in the PyPi package name with an underscore.
3. The Python module that defines the plugin's hooks/hook classes should be
   name ``<plugin>.py``.

For an example plugin that follows these conventions, have a look at
repomate-junit4_.  Granted that the plugin follows these conventions and is
installed, it can be loaded like any other ``repomate`` plugin (see `Using
Existing Plugins`_).

Hooks
=====
There are two types of hooks in ``repomate``: *core hooks* and *extension
hooks*.

Core hooks
----------
Core hooks provide core functionality for ``repomate``, and always have a
default implementation in :py:mod:`repomate.ext.defaults`. Providing a
different plugin implementation will override this behavior, thereby
changing some core part of ``repomate``. In general, only one implementation
of a core hook will run per invocation of ``repomate``. All core hooks are
defined in :py:mod:`repomate_plug.corehooks`.

Extension hooks
---------------
Extension hooks extend the functionality of ``repomate`` in various ways.
Unlike the core hooks, there are no default implementations of the extension
hooks, and multiple implementations can be run on each invocation of
``repomate``. All extension hooks are defined in
:py:mod:`repomate_plug.exthooks`. repomate-junit4_ consists solely of extension hooks,
and so do all of the `repomate built-ins`_ except for :py:mod:`repomate.ext.defaults`.

.. _repomate built-ins: https://repomate.readthedocs.io/en/latest/plugins.html#built-in-plugins
.. _repomate-junit4: https://github.com/slarse/repomate-junit4
.. _Using Existing Plugins: https://repomate.readthedocs.io/en/latest/plugins.html#using-existing-plugins
