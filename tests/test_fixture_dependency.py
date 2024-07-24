import functools

import pytest


def be_verbose(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        fn_name = function.__name__
        print("\nExecuting {}".format(fn_name))
        return function(*args, **kwargs)

    return wrapper


@pytest.fixture
@be_verbose
def order():
    return []


@pytest.fixture
@be_verbose
def append_first(order):
    order.append(1)


@pytest.fixture
@be_verbose
def append_second(order, append_first):
    order.extend([2])


@pytest.fixture(autouse=True)
@be_verbose
def append_third(order, append_second):
    order += [3]


@be_verbose
def test_order(order):
    print(order)
    assert order == [1, 2, 3]
