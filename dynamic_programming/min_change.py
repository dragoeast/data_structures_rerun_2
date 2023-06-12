def min_change(amount, coins):
    """
    Return the minimum number of coins required to create the amount.
    You may use each coin as many times as necessary.
    >>> min_change(amount=8, coins=[1, 3, 4])
    2
    >>> min_change(amount=0, coins=[1, 2, 3])
    0
    >>> min_change(amount=102, coins=[1, 5, 10, 25])
    6
    """
    result = _min_change(amount, coins, memo={})
    if result == float('inf'):
        return -1
    return result


def _min_change(amount, coins, memo):
    key = amount
    if key in memo:
        return memo[key]

    if amount < 0:
        return float('inf')
    if amount == 0:
        return 0

    min_coins = float('inf')
    for coin in coins:
        curr_coins = 1 + _min_change(amount-coin, coins, memo)
        if curr_coins < min_coins:
            min_coins = curr_coins
    memo[key] = min_coins
    return memo[key]
