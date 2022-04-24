from fastapi import APIRouter, Query
from starlette.responses import RedirectResponse

import lib_math

router = APIRouter()


@router.get("/fibonacci")
def fibonacci(n: int = Query(1, description='Number of a member of Fibonacci sequence', gt=1)):
    return lib_math.fib_generator(n)


@router.post("/ackerman")
def ackerman(m: int = Query(0, lt=4, gt=0), n: int = Query(0, gt=0)):
    result = lib_math.ack_mathematical(m, n)
    return result


@router.get("/factorial")
def factorial(n: int = Query(0, description='Non-negative number to calculate its factorial', gt=0)):
    return lib_math.fact_generator(n)


@router.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url='/docs')
