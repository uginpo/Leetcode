
def maxProfit(prices: list[int]) -> int:
    """
    Do not return anything, modify nums in-place instead.
    """
    l, r = 0, 1
    max_profit = 0
    while r < len(prices):
        profit = prices[r] - prices[l]
        match profit > 0:
            case True:
                max_profit = max(max_profit, profit)
            case False:
                l = r
        r += 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
prices = [2, 1, 2, 0, 1]
prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
