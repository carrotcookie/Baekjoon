import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    tmp = 0
    for j in range(i):
        if a[i] > a[j]:
            tmp = max(tmp, dp[j])
    dp[i] = tmp + 1

print(max(dp))