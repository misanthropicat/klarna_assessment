import pytest
from .. import lib_math
from .testdata import *


@pytest.mark.parametrize("n, exp", minimal_fact_testdata)
def test_fact_recursive(n, exp):
    assert lib_math.fact_recursive(n) == exp


@pytest.mark.parametrize("n, exp", minimal_fact_testdata + additional_fact_testdata)
def test_fact_iterative_generator(n, exp):
    assert lib_math.fact_generator(n) == exp


@pytest.mark.parametrize("n, exp", fib_testdata)
def test_fib(n, exp):
    assert lib_math.fib(n) == exp


@pytest.mark.parametrize("m, n, exp", minimal_ack_testdata)
def test_ack_recursive(m, n, exp):
    assert lib_math.ack_recursive(m, n) == exp


@pytest.mark.parametrize("m, n, exp", minimal_ack_testdata + additional_ack_testdata)
def test_ack_mathematical(m, n, exp):
    assert lib_math.ack_mathematical(m, n) == exp
