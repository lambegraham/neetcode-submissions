class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {} #O(1) avg to reference by index o(n) worst
        #RETURNS = MIN num of coins used
        def dfs(amount): #amount is remaining after we use a coin
            
            #base case
            if amount == 0:
                return 0 #no more coins can be used
            
            if amount in cache: #prev computed subproblem
                return cache[amount]

            res = float('inf') #how many coins?

            #coins = [1,2,4] O(len(coins)^amount)
            for coin in coins:
                if amount - coin >= 0: #we have remaining after using coin
                    res = min(res, 1 + dfs(amount-coin)) #return MIN num of coins used
            cache[amount] = res
            return cache[amount] #return our final answer
        answer = dfs(amount)
        return answer if answer != float('inf') else -1
    