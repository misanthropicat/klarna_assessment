from fastapi import APIRouter, Query
from starlette.responses import RedirectResponse, JSONResponse

import lib_math

router = APIRouter()


@router.get("/fibonacci")
def fibonacci(n: int = Query(1, description='Number of a member of Fibonacci sequence', ge=1)):
    return JSONResponse(content=str(lib_math.fib_generator(n)))


@router.post("/ackermann")
def ackermann(m: int = Query(0, ge=0), n: int = Query(0, ge=0)):
    return JSONResponse(content=str(lib_math.ack_mathematical(m, n)))


@router.get("/factorial")
def factorial(n: int = Query(0, description='Non-negative number to calculate its factorial', ge=0)):
    return JSONResponse(content=str(lib_math.fact_generator(n)))


@router.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url='/docs')
