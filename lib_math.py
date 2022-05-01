import time
import sys
import logging

sys.setrecursionlimit(20000)
logger = logging.getLogger(__name__)


def memoize(func):
    """
    Handles cache for calculation results of func
    """
    cache = {}
    counter = 0

    def decorate(*args):
        nonlocal counter
        logger.debug(f'recursion counter={counter}')
        if args in cache.keys():
            logger.debug(f'{func.__name__} result for args {args} is found in cache: {cache[args]}')
            return cache[args]
        else:
            counter += 1
            cache[args] = func(*args)
            logger.debug(f'{func.__name__}: result {cache[args]} for args {args} is added to cache')
            return cache[args]
    return decorate


def clock(func):
    """
    Counts function execution time
    """
    def decorate(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        logger.info('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return decorate


def fact(n: int):
    """
    Calculates factorial of number iteratively
    Returns generator object
    """
    curr = 1
    next_member = 1
    if n == 0:
        return curr
    else:
        while next_member <= n:
            curr = curr * next_member
            next_member += 1
    yield curr


@clock
@memoize
def fact_recursive(n: int):
    """
    Classical recursive solution for factorial of n
    """
    return n if n == 1 else n*fact_recursive(n-1)


@clock
async def fact_generator(n: int):
    """
    Solution with generator for factorial of n
    """
    return next(fact(n))


@clock
@memoize
def fib_recursive(n: int):
    """
    Classical recursive solution for finding a value of the certain Fibonacci sequence member
    :param n: number of member in sequence
    :return: value of n-th Fibonacci sequence member
    """
    if n < 2:
        return n
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib(n: int):
    """
    Calculates n-th member of Fibonacci sequence iteratively
    Returns generator object
    """
    first, second = 1, 1
    if n == 1:
        yield first
    elif n == 2:
        yield second
    else:
        result = 0
        while n > 2:
            result = first + second
            first, second = second, result
            n -= 1
        yield result


async def fib_generator(n: int):
    """
    Solution with generator for n-th member of Fibonacci sequence
    """
    return next(fib(n))


@clock
@memoize
async def ack_recursive(m: int, n: int):
    """
    Calculates Ackermann function for m and n recursively
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ack_recursive(m - 1, 1)
    else:
        return ack_recursive(m - 1, ack_recursive(m, n - 1))


async def ack_mathematical(m: int, n: int):
    """
    Calculates Ackermann function for m and n mathematically
    :return:
    """
    if m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2*n + 3
    elif m == 3:
        return 2**(n + 3) - 3
    elif n == 0:
        return await ack_mathematical(m - 1, 1)
    else:
        return await ack_mathematical(m - 1, await ack_mathematical(m, n - 1))
