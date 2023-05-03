import sys
input = sys.stdin.readline

# dp[i][j]는 i층 j번째에서 가질 수 있는 최대값

n = int(input())
dp = [[]]

for _ in range(n):
    dp.append([0] + list(map(int, input().split())))

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if j == 1:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[-1]))