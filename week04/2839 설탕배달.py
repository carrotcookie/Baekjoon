import sys
input = sys.stdin.readline

n = int(input())
dp = [sys.maxsize] * (n + 1)
dp[0] = 0

for unit_size in [3, 5]:
    for i in range(unit_size, n + 1):
        if dp[i - unit_size] != sys.maxsize:
            dp[i] = min(dp[i], dp[i - unit_size] + 1)

print(dp[-1] if dp[-1] != sys.maxsize else -1)