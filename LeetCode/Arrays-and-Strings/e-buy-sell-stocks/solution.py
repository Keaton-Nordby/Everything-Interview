class Solution(object):
    def maxProfit(self, prices):
        
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
            
        return max_profit
        
       
prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices)) # output should be 5