#1. This is a trick.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = float('inf')
        for i in prices:
            if (i < buy):
                buy = i
            else:
                max_profit += i-buy
                buy = i
                
        return max_profit

#2. This solution is more relevant to the satement of the problem. But I prefer the very first one. Because I found a trick and it is beautiful.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        max_profit_per_transaction = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i]<prices[i-1]:
                buy = prices[i]
                max_profit += max_profit_per_transaction
                max_profit_per_transaction = 0
            else:
                max_profit_per_transaction = max(max_profit_per_transaction, prices[i]-buy)
        
        return max_profit+max_profit_per_transaction
