class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0
        #minCoins = min coins we need to make amount 
        for coin in coins:
            for currentAmount in range(coin, amount + 1):
                minCoins[currentAmount] = min(
                    minCoins[currentAmount],
                    minCoins[currentAmount - coin] + 1
                )
        return minCoins[amount] if minCoins[amount] != amount+1 else -1
        

