Implementing hooks and writing internal plugins
***********************************************
Implementing a hook is fairly simple, and works the same way regardless of what
type of hook it is (core or extension). If you are working with your own fork
of RepoBee, all you have to do is write a small module implementing some hooks,
and drop it into the ``repobee.ext`` sub-package (i.e. the in directory
``repobee/ext`` in the RepoBee repo).

There are two ways to implement hooks: as standalone functions or wrapped in a
class. In the following two sections, we'll implement the
:py:func:`~repobee_plug.exthooks.CloneHook.act_on_cloned_repo` extension hook
using both techniques. Let's call the plugin ``exampleplug`` and make sure it
adheres to the plugin conventions.

Hook functions in a plugin class
================================
Wrapping hook implementations in a class inheriting from
:py:class:`~repobee_plug.pluginmeta.Plugin` is the recommended way to write
plugins for RepoBee. The class does some checks to make sure that all
public functions have hook function names, which comes in handy if you are
in the habit of misspelling stuff (aren't we all?). Doing it this way,
``exampleplug.py`` would look like this:

.. code-block:: python
    :caption: exampleplug.py

    import pathlib
    import os
    from typing import Union

    import repobee_plug as plug

    PLUGIN_NAME = 'exampleplug'

    class ExamplePlugin(plug.Plugin):
        """Example plugin that implements the act_on_cloned_repo hook."""

        def act_on_cloned_repo(
            self, path: Union[str, pathlib.Path], api,
        ) -> plug.HookResult:
            """Do something with a cloned repo.
            
            Args:
                path: Path to the student repo.
                api: A platform API instance.
            Returns:
                a plug.HookResult specifying the outcome.
            """
            return plug.HookResult(
                hook=PLUGIN_NAME, status=plug.Status.WARNING, msg="This isn't quite done")

Dropping ``exampleplug.py`` into the ``repobee.ext`` package and running
``repobee -p exampleplug clone [ADDITIONAL ARGS]`` should give some
not-so-interesting output from the plugin.

The name of the class really doesn't matter, it just needs to inherit from
:py:class:`~repobee_plug.pluginmeta.Plugin`. The name of the module and hook
functions matter, though. The name of the module must be the plugin name, and
the hook functions must have the precise names of the hooks they implement. In
fact, all public methods in a class deriving from
:py:class:`~repobee_plug.pluginmeta.Plugin` must have names of hook functions,
or the class will fail to be created. You can see that the hook returns a
:py:class:`~repobee_plug.util.HookResult`. This is used for reporting the
results in RepoBee, and is entirely optional (not all hooks support it,
though). Do note that if ``None`` is returned instead, RepoBee will not
report anything for the hook. It is recommended that hooks that can return
``HookResult`` do. For a comprehensive example of an internal plugin
implemented with a class, see the built-in `javac plugin`_.

Standalone hook functions
=========================
Using standalone hook functions is recommended only if you don't want the
safety net provided by the :py:class:`~repobee_plug.pluginmeta.Plugin`
metaclass. It is fairly straightforward: simply mark a function with the
:py:const:`repobee_plug.repobee_hook` decorator. With this approach,
``exampleplug.py`` would look like this:

.. code-block:: python
    :caption: exampleplug.py

    import pathlib
    import os
    from typing import Union

    import repobee_plug as plug

    PLUGIN_NAME = 'exampleplug'

    @plug.repobee_hook
    def act_on_cloned_repo(path: Union[str, pathlib.Path]) -> plug.HookResult:
        """Do something with a cloned repo.
        
        Args:
            path: Path to the student repo.
        Returns:
            a plug.HookResult specifying the outcome.
        """
        return plug.HookResult(
            hook=PLUGIN_NAME, status=plug.Status.WARNING, msg="This isn't quite done")

Again, dropping ``exampleplug.py`` into the ``repobee.ext`` package and running
``repobee -p exampleplug clone [ADDITIONAL ARGS]`` should give some
not-so-interesting output from the plugin. For a more practical example of a
plugin implemented using only a hook function, see the built-in `pylint
plugin`_.

.. _repobee-junit4: https://github.com/repobee/repobee-junit4
.. _javac plugin: https://github.com/repobee/repobee/blob/master/repobee/ext/javac.py
.. _pylint plugin: https://github.com/repobee/repobee/blob/master/repobee/ext/pylint.py
