import sys
input = sys.stdin.readline

# n = int(input())
# a = list(map(int, input().split()))

# tmp = 0
# ans = -sys.maxsize

# for i in range(n):
#     tmp += a[i]
#     ans = max(ans, tmp)

#     if tmp < 0:
#         tmp = 0

# print(ans)

#############################################################################

# dp[i]는 위치 i까지 연속합의 최대

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [-sys.maxsize] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(a[i], dp[i - 1] + a[i])

print(max(dp))