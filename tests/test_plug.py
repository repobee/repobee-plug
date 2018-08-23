from repomate_plug import plug


class TestPlugin:
    """Tests for the Plugin wrapper class."""
    from repomate_plug import plug

    def test_class_with_no_args(self):
        """Test that the class itself is an instance of Plugin, and that the
        class can be instantiated.
        """

        @plug.Plugin
        class TestClass:
            pass

        assert isinstance(TestClass, plug.Plugin)
        assert TestClass()

    def test_class_with_args(self):
        """Test that the class is an instance of Plugin, and that positional
        arguments are passed on correctly.
        """

        @plug.Plugin
        class TestClass:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        x_expected = 87
        y_expected = "hello"

        inst = TestClass(x_expected, y_expected)

        assert isinstance(TestClass, plug.Plugin)
        assert inst.x == x_expected
        assert inst.y == y_expected

    def test_class_with_kwargs(self):
        """Test that the class is an instance of Plugin, and that keyword
        arguments are passed on correctly.
        """

        @plug.Plugin
        class TestClass:
            def __init__(self, *, x, y):
                self.x = x
                self.y = y

        x_expected = 87
        y_expected = "hello"

        inst = TestClass(x=x_expected, y=y_expected)

        assert isinstance(TestClass, plug.Plugin)
        assert inst.x == x_expected
        assert inst.y == y_expected

    def test_class_with_args_and_kwargs(self):
        @plug.Plugin
        class TestClass:
            def __init__(self, x_arg, y_arg, *, x_kwarg, y_kwarg):
                self.x_arg = x_arg
                self.y_arg = y_arg
                self.x_kwarg = x_kwarg
                self.y_kwarg = y_kwarg

        x_arg_expected = 123
        y_arg_expected = "hithere"
        x_kwarg_expected = -9
        y_kwarg_expected = 88

        inst = TestClass(
            x_arg_expected,
            y_arg_expected,
            x_kwarg=x_kwarg_expected,
            y_kwarg=y_kwarg_expected)

        assert inst.x_arg == x_arg_expected
        assert inst.y_arg == y_arg_expected
        assert inst.x_kwarg == x_kwarg_expected
        assert inst.y_kwarg == y_kwarg_expected
