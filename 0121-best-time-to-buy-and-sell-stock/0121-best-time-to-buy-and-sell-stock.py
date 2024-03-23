class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        
        l,r =0,1
        while r< len(prices):
            if prices[l]< prices[r]:
                Profit = prices[r]- prices[l]
                maxProfit = max(maxProfit,Profit)
            else:
                l=r
            r+=1
        return maxProfit
            
            