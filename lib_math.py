import time
import sys

sys.setrecursionlimit(200000)


def memoize(func):
    cache = {}
    counter = 0

    def decorate(*args):
        nonlocal counter
        print(f'recursion counter={counter}')
        if args in cache.keys():
            print(f'{func.__name__} result for args {args} is found in cache: {cache[args]}')
            return cache[args]
        else:
            counter += 1
            cache[args] = func(*args)
            print(f'{func.__name__}: result {cache[args]} for args {args} is added to cache')
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
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return decorate


@clock
@memoize
def fact(n: int):
    if n == 1:
        return n
    else:
        return n*fact(n-1)


@clock
@memoize
def fib(n: int):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


@memoize
def ack(m: int, n: int):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))
