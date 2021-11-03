import sys
def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [sys.maxsize]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[-1] == sys.maxsize:
        return  -1
    return dp[-1]