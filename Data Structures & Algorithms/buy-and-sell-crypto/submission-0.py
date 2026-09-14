class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        high = 0

        for i in range(len(prices)-1):
            for j in range(len(prices[i:])):
                high =  max(high, prices[j+i] - prices[i])
        return high