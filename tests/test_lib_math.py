import pytest
from .. import lib_math
from .testdata import *


@pytest.mark.parametrize("n, exp", fact_testdata)
def test_fact(n, exp):
    assert lib_math.fact(n) == exp


@pytest.mark.parametrize("n, exp", fib_testdata)
def test_fib(n, exp):
    assert lib_math.fib(n) == exp


@pytest.mark.parametrize("m, n, exp", ack_testdata)
def test_ack(m, n, exp):
    assert lib_math.ack(m, n) == exp
