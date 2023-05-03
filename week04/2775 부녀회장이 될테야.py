import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for b in range(1, n + 1):
        dp[0][b] = b

    for a in range(1, k + 1):
        for b in range(1, n + 1):
            for c in range(b):
                dp[a][b] += dp[a - 1][b - c]
    
    print(dp[k][n])