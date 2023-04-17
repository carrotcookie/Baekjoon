import sys

# 1. 2중 for문 최대 2500억 연산.....
# n = int(input())
# a = list(map(int, sys.stdin.readline().split()))
# dp = [0] * n

# for i in range(n):
#     for j in range(i - 1, -1, -1):
#         if a[i] < a[j]:
#             dp[i] = j + 1
#             break
#         dp[i] = 0

# print(*dp)

######################################################################################################################

# 2. 스택
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
stack = []

for i in range(n):
    while stack and stack[-1][0] < a[i]:
        stack.pop()

    if stack:
        dp[i] = stack[-1][1] + 1
    else:
        dp[i] = 0

    stack.append((a[i], i))

print(*dp)