n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
dp[0] = 0
dp[1] = abs(a[1] - a[0])

for i in range(2, n):
    min_val = a[i]
    max_val = a[i]

    for j in range(i - 1, -1, -1):
        min_val = min(min_val, a[j])
        max_val = max(max_val, a[j])
        dp[i] = max(dp[i], dp[j] + max_val - min_val)

print(dp[-1])
print(dp)