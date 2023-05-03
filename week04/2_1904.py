import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

if n >= 2:
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] % 15746 + dp[i - 2] % 15746) % 15746

    print(dp[n])
else:
    print(1)