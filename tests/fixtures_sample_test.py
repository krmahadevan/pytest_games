import pytest
from _pytest.fixtures import FixtureRequest


def setup_module(module):
    """
    A setup method that gets executed ONLY once per module
    :param module: This represents the current module i.e., the file name is the module name in the python world
    :return:
    """
    print(f"\n\t[ModuleSetup] for module {module.__name__}")


def teardown_module(module):
    """
    A teardown method that gets executed ONLY once per module
    :param module: This represents the current module i.e., the file name is the module name in the python world
    :return:
    """
    print(f"\n\t[ModuleTeardown] for module {module.__name__}")


def test_normal_method():
    """
    This is a normal test method that does not belong to any class
    """
    print(f"\n\t[TestNormalMethod]")


class TestGrandpa:

    @classmethod
    @pytest.fixture(autouse=True)
    def setup_at_class_level(cls):
        """
        This setup method gets executed twice because there's a data driven test that will run for 2 methods
        """
        print(f"\n\t[ClassSetup] for class {type(cls).__name__}")

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def teardown_at_class_level(cls):
        """
        This setup method gets executed ONLY once per class even though there are two 2 methods because the scope
        is defined as "class".

        If no scope is defined, then it defaults to "function" i.e., test method
        """
        print(f"\n\t[ClassTeardown] for class {type(cls).__name__}")


class TestParent(TestGrandpa):

    @pytest.fixture(autouse=True)
    def setup_at_method_level(self, request: FixtureRequest):
        print(f"\n\t[MethodSetup] for method {request.node.name}")
        node = request.node
        if isinstance(node, pytest.Function):
            print("Node ", node)
            for marker in node.own_markers:
                for arg in marker.args:
                    if isinstance(arg, tuple):
                        print(f"Length = {len(arg)}, {str(arg)}")
                        key, value = arg
                        print(f"\t{key} = {value}")

    @pytest.fixture(autouse=True)
    def teardown_at_method_level(self, request):
        print(f"\n\t[MethodTeardown] for method {request.node.name}")


class TestChild(TestParent):

    def test_say_hello(self):
        print("test_say_hello() called")


class TestDataDrivenChild(TestParent):

    @pytest.mark.parametrize("country, is_beautiful", [("India", True), ("Phantom", False)])
    def test_print_countries(self, country, is_beautiful: bool):
        if is_beautiful:
            print(f"\n\t[DataDrivenChild] {country} is beautiful")
        else:
            print(f"\n\t[DataDrivenChild] {country} is horrible")
