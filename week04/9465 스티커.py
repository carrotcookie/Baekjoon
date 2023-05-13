import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = a[0][0]
    dp[0][1] = a[1][0]

    if n == 1:
        print(max(a[0][0], a[1][0]))
        continue

    for i in range(1, n):
        for j in range(2):
            dp[i][j] = max(dp[i - 1][not j] + a[j][i], dp[i - 1][j])
    
    print(max(dp[-1]))