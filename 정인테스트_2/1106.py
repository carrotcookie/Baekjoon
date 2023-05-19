import sys
input = sys.stdin.readline

c, n = map(int, input().split())
dp = [[sys.maxsize] * (c + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    cost, amount = map(int, input().split())

    for j in range(1, c + 1):
        dp[i][j] = dp[i - 1][j]

        k = 0
        while True:
            if j - (k * amount) <= 0:
                dp[i][j] = min(dp[i][j], k * cost)
                break
            
            dp[i][j] = min(dp[i][j], dp[i - 1][j - k * amount] + k * cost)
            k += 1

print(dp[-1][-1])