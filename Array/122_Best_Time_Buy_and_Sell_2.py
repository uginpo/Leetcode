
def maxProfit(prices: list[int]) -> int:
    """
    Do not return anything, modify nums in-place instead.
    """
    profit = [prices[r] - prices[r-1] for r in range(1, len(prices))]
    max_profit = sum(map(lambda x: x if x > 0 else 0, profit))

    return max_profit


prices = [2, 1, 2, 0, 1]
prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
