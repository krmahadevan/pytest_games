import pytest


@pytest.mark.parametrize("number,is_even",
                         [
                             (10, True),
                             (1, False),
                             # Here we are saying that we know that this data combo is expected to fail
                             pytest.param(98, False, marks=pytest.mark.xfail),
                         ])
def test_sample_function(number: int, is_even: bool):
    assert (number % 2 == 0) == is_even
