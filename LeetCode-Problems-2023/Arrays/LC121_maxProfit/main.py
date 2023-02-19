class Solution:
    def maxProfit(self, prices):
        max_profit = 0 
        previous_min = prices[0]
        
        for p in prices[1::]:
            current_profit = p - previous_min
            max_profit = max(max_profit, current_profit)
            
            previous_min = min(previous_min, p)
        
        return max_profit
        
    
a = Solution()
print(a.maxProfit([2,1,4]))
    
            
