class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = float('inf')
        for p in prices:
            if p < min_so_far:
                min_so_far = p
            else:
                max_profit = max(max_profit, (p - min_so_far))
        return max_profit