import sys
input = sys.stdin.readline
INF = sys.maxsize

# 1. 1로 만들기
# x = int(input())
# dp = [INF] * (x + 1)
# dp[1] = 0

# for i in range(2, x + 1):
#     if not i % 2:
#         dp[i] = min(dp[i // 2], dp[i - 1]) + 1
#     if not i % 3:
#         dp[i] = min(dp[i // 3], dp[i - 1]) + 1
#     if not i % 5:
#         dp[i] = min(dp[i // 5], dp[i - 1]) + 1

# print(dp[x])

############################################################################################################################

# 2. 효율적인 화폐 구성
# n, m = map(int, input().split())
# maximum = m + 1
# dp = [maximum] * (m + 1)
# dp[0] = 0

# for _ in range(n):
#     coin = int(input())
#     for i in range(coin, m + 1):
#         if dp[i - coin] != maximum:
#             dp[i] = min(dp[i], dp[i - coin] + 1)

# print(dp[m] if dp[m] != maximum else -1)

############################################################################################################################
 
T = int(input())
k = 0
coin = [1, 10, 25]

while T:
    T -= 1
    x = int(input())
    ans = 0
    dp = [10**15+1 for _ in range(100)]
    dp[0] = 0
    for c in coin:
        for i in range(c, 100):
            dp[i] = min(dp[i], dp[i-c]+1)
    print(dp)
    while x:
        ans += dp[x % 100]
        x //= 100
    print(ans)