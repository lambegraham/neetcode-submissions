class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #buy 1, 1 day cooldown
        #don't buy 1, 0 cooldown
        #can only hold 1 at a time
        cache = {}
        def dfs(i, holding): #holding = must sell
            if (i, holding) in cache:
                return cache[(i, holding)]

            if i >= len(prices):
                return 0 #no more days to make profit
            
            cooldown = dfs(i + 1, holding) #skip current day
                
            if not holding: #buy case, continue tomorrow
                buy = dfs(i + 1, not holding) - prices[i] #next day, buy
                cache[(i, holding)] = max(buy, cooldown)
                return cache[(i, holding)]

            else: #sell today, skip tomorrow
                sell = dfs(i + 2, not holding) + prices[i] 
                cache[(i, holding)] = max(sell, cooldown)
                return cache[(i, holding)]
        return dfs(0, False) #start not holding