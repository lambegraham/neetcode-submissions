class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #inf is placeholder
        dp = [float("inf")] * (amount + 1) #amount is target 0..amount
        #to compute 0 it takes 0 coins
        dp[0] = 0

        #from 1 to amount+1
        for a in range(1, amount+1):
            #for coins
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                #non negative, so we could have a sol
                #dp is either min of dp or new dp
        return dp[amount] if dp[amount] != float("inf") else -1
                # +1 comes from extra coint
                # coin = 4, a = 7 ... 4-7 = 3 WE NEED 3
                # dp[7] = 1 + dp[3] is less than dp[a]

        #return dp amount, if not DEFAULT VALUE (amount+1)