import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [sys.maxsize] * (k + 1)
dp[-1] = 0

if k % 2 != 0:
    dp = dp + [sys.maxsize]

dp[-1] = 1

print(dp)

length = len(dp)

for i in range(length - 3, -1, -1):
    dp[i] = dp[i + 1] + 1

    if i * 2 <= length:
        dp[i] = min(dp[i], dp[2 * i])
    
print(dp)