class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        #going to need to loop through prices

        #brute force
        for i in range(len(prices)):

            for j in range(len(prices) - i):
                if prices[j+i] - prices[i] > max_profit:
                    max_profit = prices[j+i] - prices[i]
        return max_profit
        #O(nlogn) time, O(1) space