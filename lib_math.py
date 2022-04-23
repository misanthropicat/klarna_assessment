def fact(n: int):
    if n == 1:
        return n
    else:
        return n*fact(n-1)


def fib_gen(n: int):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def ack(m: int, n: int):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1, 1)
