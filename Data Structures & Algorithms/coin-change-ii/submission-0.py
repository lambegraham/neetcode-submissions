class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, amount):

            if amount == 0: #got amount
                return 1
            if i >= len(coins): #went past coins
                return 0
            if (i, amount) in cache:
                return cache[(i, amount)]

            # res = 0
            res = dfs(i + 1, amount) #don't pick coin, continue
            if amount >= coins[i]: #pick coin
                res += dfs(i, amount - coins[i]) #pick coin, minus it
            cache[(i, amount)] = res
            return cache[(i, amount)]
        return dfs(0, amount)