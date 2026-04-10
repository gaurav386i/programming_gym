
"""
5) Best Time to Buy and Sell Stock

Topic: Array
Difficulty: Easy
Given an array where prices[i] is the price of a stock on day i, 
find the maximum profit you can achieve by buying once and selling once.
"""
def max_profit(prices: list[int]) -> int:
    """
    
    """
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else: 
            max_profit = max(max_profit, price - min_price)
    return max_profit

if __name__ == "__main__":
    prices = [123, 23, 45, 55, 13, 250, 44, 21, 100]
    max_profit(prices)
