import pytest
import pluggy
from repomate_plug import pluginmeta
from repomate_plug import exception


class TestPluginInheritance:
    def test_raises_on_non_hook_public_method(self):
        with pytest.raises(exception.HookNameError) as exc:

            class Derived(pluginmeta.Plugin):
                """Has the hook method config_hook and a non-hook method called
                some_method."""

                def config_hook(self, config_parser):
                    pass

                def some_method(self, x, y):
                    return x + y

        assert "public method(s) with non-hook name" in str(exc)
        assert "some_method" in str(exc)
        assert "config_hook" not in str(exc)

    def test_happy_path(self):
        """Test that a class can be defined when all public methods are have
        hook names.
        """

        class Derived(pluginmeta.Plugin):
            """Has all four hook methods defined."""

            def act_on_cloned_repo(self, path):
                pass

            def clone_parser_hook(self, clone_parser):
                pass

            def parse_args(self, args):
                pass

            def config_hook(self, config_parser):
                pass

    def test_with_private_methods(self):
        """Private methods should be able to have any names."""

        class Derived(pluginmeta.Plugin):
            """Has all four hook methods defined."""

            def act_on_cloned_repo(self, path):
                pass

            def clone_parser_hook(self, clone_parser):
                pass

            def parse_args(self, args):
                pass

            def config_hook(self, config_parser):
                pass

            def _some_method(self, x, y):
                return x + y

            def _other_method(self):
                return self
