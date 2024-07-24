import pytest

input_data_set = [(10, True), (1, False)]

data_set_names = ["Ensure 10 is even", "Ensure 1 is odd"]


def pytest_generate_tests(metafunc):
    print(f"======> {metafunc.fixturenames}")


@pytest.mark.parametrize("number,is_even", input_data_set, ids=data_set_names)
def test_with_custom_names(number: int, is_even: bool):
    assert (number % 2 == 0) == is_even


numbers = {
    1: "One",
    10: "Ten"
}


def id_generator(in_value):
    if type(in_value) is int:
        return numbers[in_value]

    if type(in_value) is bool:
        if in_value:
            return "Yes"
        return "No"
    return f"Input--{in_value}"


@pytest.mark.parametrize("number,is_even", input_data_set, ids=id_generator)
def test_with_dynamic_names(number: int, is_even: bool):
    assert (number % 2 == 0) == is_even


@pytest.mark.parametrize(
    "number,is_even",
    [
        pytest.param(1, False, id="One-is-odd"),
        pytest.param(10, True, id="Ten-is-even")
    ]
)
def test_another_way_to_provide_custom_test_names(number: int, is_even: bool):
    assert (number % 2 == 0) == is_even
