class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        mimimum=prices[l]
        for r in range(len(prices)):
            currlow=prices[l]
            l += 1 
            mimimum=min(mimimum,currlow)
            curr=prices[r]-mimimum
            profit=max(profit,curr)
        return profit
            

        