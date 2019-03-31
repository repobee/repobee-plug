Plugin system overview
**********************

Conventions
===========
For ``repobee`` to discover a plugin and its hooks, the following conventions
need to be adhered to:

1. The PyPi package should be named ``repobee-<plugin>``, where ``<plugin>``
   is the name of the plugin.
2. The actual Python package (i.e. the directory in which the source files
   are located) should be called ``repobee_<plugin>``. In other words,
   replace the hyphen in the PyPi package name with an underscore.
3. The Python module that defines the plugin's hooks/hook classes should be
   name ``<plugin>.py``.

For an example plugin that follows these conventions, have a look at
repobee-junit4_.  Granted that the plugin follows these conventions and is
installed, it can be loaded like any other ``repobee`` plugin (see `Using
Existing Plugins`_).

Hooks
=====
There are two types of hooks in ``repobee``: *core hooks* and *extension
hooks*.

Core hooks
----------
Core hooks provide core functionality for ``repobee``, and always have a
default implementation in :py:mod:`repobee.ext.defaults`. Providing a
different plugin implementation will override this behavior, thereby
changing some core part of ``repobee``. In general, only one implementation
of a core hook will run per invocation of ``repobee``. All core hooks are
defined in :py:mod:`repobee_plug.corehooks`.

Extension hooks
---------------
Extension hooks extend the functionality of ``repobee`` in various ways.
Unlike the core hooks, there are no default implementations of the extension
hooks, and multiple implementations can be run on each invocation of
``repobee``. All extension hooks are defined in
:py:mod:`repobee_plug.exthooks`. repobee-junit4_ consists solely of extension hooks,
and so do all of the `repobee built-ins`_ except for :py:mod:`repobee.ext.defaults`.

.. _repobee built-ins: https://repobee.readthedocs.io/en/latest/plugins.html#built-in-plugins
.. _repobee-junit4: https://github.com/repobee/repobee-junit4
.. _Using Existing Plugins: https://repobee.readthedocs.io/en/latest/plugins.html#using-existing-plugins
