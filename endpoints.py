from fastapi import APIRouter, Query
from models import Ackerman

router = APIRouter()


@router.get("/fibonacci")
def fibonacci(n: int = Query()):
    result = n
    return result


@router.post("/ackerman")
def ackerman(payload: Ackerman):
    result = payload.m * payload.n
    return result


@router.get("/factorial")
def factorial(n: int = 0):
    return 


@router.get('/')
def multiply(n: int = 0):
    return n * n
