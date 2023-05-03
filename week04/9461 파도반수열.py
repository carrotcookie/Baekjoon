import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())
    dp = [0, 1, 1, 1]

    if n == 1 or n == 2 or n == 3:
        print(dp[1])
    else:
        for i in range(4, n + 1):
            dp.append(dp[i - 2] + dp[i - 3])
        print(dp[-1])