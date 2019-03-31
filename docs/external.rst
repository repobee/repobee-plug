Writing external plugins (recommended and easy!)
************************************************
Writing an external plugin is really easy using the
repobee-plugin-cookiecutter_ template. First of all, you need to install
cookiecutter_. It's on PyPi and installs just the same as ``repobee`` with
``pip install cookiecutter`` (with whatever flags you like to use). Now,
running ``python3 -m cookiecutter gh:repobee/repobee-plugin-cookiecutter``
will give you some prompts to answer. If you want to create a plugin called
``exampleplug``, it looks something like this:

.. code-block:: bash

    $ python3 -m cookiecutter gh:repobee/repobee-plugin-cookiecutter
    author []: Your Name
    email []: email@address.com
    github_username []: your_github_username
    plugin_name []: exampleplug
    short_description []: An example plugin!

This will result in a directory called ``repobee-exampleplug``, containing a
fully functioning (albeit quite useless) external plugin. If you do ``cd
exampleplug`` and then run ``pip install -e .``, you will install the plugin
locally. You can then use it like any of the built-in plugins, as described in
`Using Existing Plugins`_. To actually implement the behavior that you want,
edit the file ``repobee-exampleplug/repobee_exampleplug/exampleplug.py`` to
implement the hooks you want.

.. _repobee-plugin-cookiecutter: https://github.com/repobee/repobee-plugin-cookiecutter
.. _cookiecutter: https://github.com/audreyr/cookiecutter-pypackage
.. _Using Existing Plugins: https://repobee.readthedocs.io/en/latest/plugins.html#using-existing-plugins
