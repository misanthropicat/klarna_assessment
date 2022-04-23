import time
import sys
import logging

sys.setrecursionlimit(20000)
logger = logging.getLogger(__file__)
file_handler = logging.Handler('DEBUG')
console_handler = logging.Handler('INFO')
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def memoize(func):
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
    :param n:
    :return:
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
    return n if n == 1 else n*fact_recursive(n-1)


@clock
def fact_generator(n: int):
    return next(fact(n))


@clock
@memoize
def fib(n: int):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


@memoize
def ack_recursive(m: int, n: int):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack_recursive(m - 1, 1)
    else:
        return ack_recursive(m - 1, ack_recursive(m, n - 1))


@clock
def ack_mathematical(m: int, n: int):
    if m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2*n + 3
    elif m == 3:
        return 8*(2**n - 1) + 5
    elif n == 0:
        return ack_mathematical(m - 1, 1)
    else:
        return ack_mathematical(m - 1, ack_mathematical(m, n - 1))
