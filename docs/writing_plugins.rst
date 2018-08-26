Writing Plugins
***************

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

For an example plugin that follows these conventions, have a look at repomate-junit4_.

Hooks
=====
The available hooks are defined in the
:py:class:`~repomate_plug.hookspec.CloneHook` class. For detailed information
on the hooks, refer to the documentation of
:py:class:`repomate_plug.hookspec.CloneHook`.

This section will be fleshed out more in the future. For now, refer to
repomate-junit4_ as an example, as well as the `repomate built-ins`_

.. _repomate built-ins: https://repomate.readthedocs.io/en/latest/plugins.html#built-in-plugins
.. _repomate-junit4: https://github.com/slarse/repomate-junit4
