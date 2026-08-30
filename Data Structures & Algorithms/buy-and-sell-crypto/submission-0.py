class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof=0
        min_prof = float('inf')
        

        for i in range(len(prices)):

            min_prof=min(min_prof,prices[i])
            max_prof=max(max_prof,prices[i]-min_prof)

        return max_prof    