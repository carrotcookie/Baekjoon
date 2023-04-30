import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
dp = [[sys.maxsize] * n for _ in range(n)]

for i in range(n):
    for j in range(n - i):
        x = j
        y = i + j

        if x == y:
            dp[x][y] = 0
        elif y - x == 1:
            dp[x][y] = info[x][0] * info[x][1] * info[y][1]
        else:
            for k in range(x, y):
                dp[x][y] = min(dp[x][y], dp[x][k] + dp[k + 1][y] + info[x][0] * info[k][1] * info[y][1])

print(dp[0][n - 1])