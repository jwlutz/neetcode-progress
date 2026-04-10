class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = float('inf')
        #iterate through prices, if find a higher price, look for min value to the left of it
        for p in prices:
            if p < min_value:
                min_value = p
            else:
                max_profit = max(max_profit, (p - min_value))
        return max_profit
        #O(n) time, O(1) space