class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        mimimum=prices[l]
        for r in range(1,len(prices)):
            mimimum=min(mimimum,prices[r])
            curr=prices[r]-mimimum
            profit=max(profit,curr)
        return profit
            

        