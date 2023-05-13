import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for col in range(1, k + 1):
    dp[1][col] = col

for i in range(2, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[-1][-1] % 1000000000)