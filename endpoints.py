from fastapi import APIRouter, Query
from models import Ackerman
import lib_math

router = APIRouter()


@router.get("/fibonacci")
def fibonacci(n: int = Query(1, description='Number of a member of Fibonacci sequence', gt=1)):
    return lib_math.fib_gen(n)


@router.post("/ackerman")
def ackerman(payload: Ackerman):
    result = payload.m * payload.n
    return result


@router.get("/factorial")
def factorial(n: int = Query(0, description='Non-negative number to calculate its factorial', gt=0)):
    return lib_math.fact(n)
