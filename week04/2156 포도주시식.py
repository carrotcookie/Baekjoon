import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = a[0]
dp[1] = a[0] + a[1]
dp[2] = max(a[0] + a[1], a[1] + a[2], dp[1])

for i in range(3, n):
    dp[i] = max(a[i] + dp[i - 2], a[i] + a[i - 1] + dp[i - 3], dp[i - 1])

print(dp[-1])