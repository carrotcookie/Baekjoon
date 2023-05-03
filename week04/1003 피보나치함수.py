import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    dp = []
    dp.append((1, 0))
    dp.append((0, 1))

    for i in range(2, n + 1):
        tmp = [dp[i - 1][j] + dp[i - 2][j] for j in range(2)]
        dp.append(tmp)
    
    print(*dp[n])