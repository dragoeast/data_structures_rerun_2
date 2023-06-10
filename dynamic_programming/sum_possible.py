def sum_possible(amount, coins):
    """Return True if it is possible to make the amount with the coins.
    Otherwise False.
    >>> sum_possible(amount=10, coins=[3, 2, 5, 7])
    True
    >>> sum_possible(amount=11, coins=[3, 7])
    False
    >>> sum_possible(amount=2023, coins=[2, 5, 10])
    False
    """
    return _sum_possible(amount, coins, memo={})


def _sum_possible(amount, coins, memo):
    key = amount
    if key in memo:
        return memo[key]

    if amount == 0:
        return True
    if amount < 0:
        return False

    for coin in coins:
        if _sum_possible(amount-coin, coins, memo) == True:
            memo[key] = True
            return memo[key]
    memo[key] = False
    return memo[key]
