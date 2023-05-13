import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [sys.maxsize] * n

dp[0] = 0
for i in range(n):
    for j in range(i):
        # 이전 위치 j에서 현재위치 i까지 도약 가능하면
        if a[j] + j >= i:
            dp[i] = min(dp[i], dp[j] + 1)

print(dp[-1] if dp[-1] != sys.maxsize else -1)