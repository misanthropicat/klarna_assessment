import pytest
from fastapi.testclient import TestClient

from .testdata import *
from ..app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.parametrize("n, exp", minimal_fact_testdata)
def test_factorial(n, exp):
    response = client.get(f'/factorial?n={n}')
    assert response.status_code == 200
    assert int(response.content) == exp


@pytest.mark.parametrize("n, exp", minimal_fib_testdata)
def test_fibonacci(n, exp):
    response= client.get(f'/fibonacci?n={n}')
    assert response.status_code == 200
    assert int(response.content) == exp


@pytest.mark.parametrize("m, n, exp", minimal_ack_testdata)
def test_ackermann(m, n, exp):
    response = client.post(f'/ackermann?m={m}&n={n}')
    assert response.status_code == 200
    assert int(response.content) == exp
