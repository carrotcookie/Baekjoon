import sys
input = sys.stdin.readline

# dp[i][j]는 i번째 집을 j색깔로 칠했을 때 i번째 집까지 칠하는데 최소비용

n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = list(map(int, input().split()))

for i in range(2, n + 1):
    for j in range(3):
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j - 2]) + dp[i][j]

print(min(dp[-1]))