def fib(n):
    """
    >>> [ fib(n) for n in range(8) ]
    [0, 1, 1, 2, 3, 5, 8, 13]
    """
    return _fib(n, memo={})


def _fib(n, memo):
    key = n
    if key in memo:
        return memo[key]

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[key] = fib(n-1) + fib(n-2)
    return memo[key]
