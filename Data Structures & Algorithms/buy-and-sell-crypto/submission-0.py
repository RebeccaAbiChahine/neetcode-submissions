class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0 # sell
        right = 1 # buy

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1 

        return maxProfit


