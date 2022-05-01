import time

from fastapi import APIRouter, Query
from starlette.responses import RedirectResponse, JSONResponse

import lib_math

router = APIRouter()


@router.get("/fibonacci")
async def fibonacci(n: int = Query(1, description='Number of a member of Fibonacci sequence', ge=1)):
    start = time.time()
    lib_math.logger.info('STARTED: %s(%s)', router.url_path_for('fibonacci'), n)
    result = await lib_math.fib_generator(n)
    elapsed = time.time() - start
    lib_math.logger.info('DONE: [%0.8fs] %s(%s)', elapsed, router.url_path_for('fibonacci'), n)
    return JSONResponse(content=str(result))


@router.post("/ackermann")
async def ackermann(m: int = Query(0, ge=0), n: int = Query(0, ge=0)):
    start = time.time()
    lib_math.logger.info('STARTED: %s(%s)', router.url_path_for('ackermann'), f'{m},{n}')
    result = await lib_math.ack_mathematical(m, n)
    elapsed = time.time() - start
    lib_math.logger.info('DONE: [%0.8fs] %s(%s)', elapsed, router.url_path_for('ackermann'), f'{m},{n}')
    return JSONResponse(content=str(result))


@router.get("/factorial")
async def factorial(n: int = Query(0, description='Non-negative number to calculate its factorial', ge=0)):
    start = time.time()
    lib_math.logger.info('STARTED: %s(%s)', router.url_path_for('factorial'), n)
    result = await lib_math.fact_generator(n)
    elapsed = time.time() - start
    lib_math.logger.info('DONE: [%0.8fs] %s(%s)' % (elapsed, router.url_path_for('factorial'), n))
    return JSONResponse(content=str(result))


@router.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url='/docs')
