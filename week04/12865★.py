import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = []
dp = [[0] * (k + 1) for _ in range(n)]

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

for i in range(n):
    for j in range(1, k + 1):
        w, v = items[i]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
            
print(dp[-1][-1])
print()
for i in range(n):
    for j in range(1, k + 1):
        print(f'{dp[i][j]:>3}', end = '')
    print()