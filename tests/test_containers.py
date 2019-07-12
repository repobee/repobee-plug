import argparse
import pytest
from repobee_plug import containers
from repobee_plug import exception


class TestExtensionCommand:
    def test_raises_if_parser_is_not_a_ExtensionParser(self):
        parser = argparse.ArgumentParser()

        with pytest.raises(exception.ExtensionCommandError) as exc_info:
            containers.ExtensionCommand(
                parser, "test-command", "help", "description", lambda args, api: None
            )

        assert "parser must be a ExtensionParser" in str(exc_info.value)

    def test_raises_if_callback_is_not_callable(self):
        callback = 2

        with pytest.raises(exception.ExtensionCommandError) as exc_info:
            containers.ExtensionCommand(
                containers.ExtensionParser(),
                "test-command",
                "help",
                "description",
                callback,
            )

    def test_requires_api_false_by_default(self):
        exc_command = containers.ExtensionCommand(
            containers.ExtensionParser(),
            "test-command",
            "help",
            "description",
            lambda args, api: None,
        )

        assert not exc_command.requires_api

    def test_eq_with_unequal_parsers(self):
        """ExtensionCommands should compare equal if all attributes but the
        parser are the same. The reason for this is that
        argparse.ArgumentParser instances don't compare equal even if they are.
        """
        lhs_parser = containers.ExtensionParser()
        rhs_parser = containers.ExtensionParser()
        assert lhs_parser != rhs_parser, "parsers should be unequal"
        command_name = "test-command"
        help = "help"
        description = "description"

        def callback(args, api):
            return None

        lhs = containers.ExtensionCommand(
            lhs_parser, command_name, help, description, callback
        )
        rhs = containers.ExtensionCommand(
            lhs_parser, command_name, help, description, callback
        )

        assert lhs == rhs
