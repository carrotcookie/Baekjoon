import sys

# 1. 정렬 되어있는 배열이 있을 때
#    입력되는 원소 n의 위치
# a = [1, 2, 2, 2, 3, 5, 6, 7, 7]

# while True:
#     n = int(input())

#     left = 0
#     right = len(a) - 1
#     result_idx = -1

#     while left <= right:
#         mid = (left + right) // 2

#         # # 같은 값이 있다면 왼쪽
#         if a[mid] >= n: 
#             right = mid - 1
#             result_idx = mid
#         else:
#             left = mid + 1
#             result_idx = mid + 1

#         # # 같은 값이 있다면 오른쪽
#         # if a[mid] > n: 
#         #     right = mid - 1
#         #     result_idx = mid
#         # else:
#         #     left = mid + 1
#         #     result_idx = mid + 1


#     if result_idx > -1:
#         print(f'{n}은 {a}에서 [{result_idx}]에 넣을 수 있습니다.')
#     else:
#         print(f'{n}은 {a}에 존재하지 않습니다.')

#######################################################################################################################

# 개미전사
# n = int(input())
# a = list(map(int, sys.stdin.readline().split()))
# dp = [0] * n

# dp[0] = a[0]
# dp[1] = max(a[0], a[1])

# for i in range(2, n):
#     dp[i] = max(dp[i-1], dp[i-2] + a[i])

# print(dp[-1])

#######################################################################################################################

# 입력받은 숫자 1로 만드는 최단거리
# x = int(input())
# dp = [0] * (x + 1)

# dp[1] = 0

# for i in range(2, x + 1):
#     dp[i] = dp[i - 1] + 1

#     if i % 2 == 0:
#         dp[i] = min(dp[i - 1], dp[i // 2]) + 1
#     if i % 3 == 0:
#         dp[i] = min(dp[i - 1], dp[i // 3]) + 1
#     if i % 5 == 0:
#         dp[i] = min(dp[i - 1], dp[i // 5]) + 1

# print(dp[-1])

#######################################################################################################################

# 화폐 종류 n가지로 m원을 만들 수 있는 최소개수 dp로 풀기
# n, m = map(int, input().split())
# dp = [sys.maxsize] * (m + 1)

# dp[0] = 0
# for _ in range(n):

#     k_won = int(sys.stdin.readline())

#     for i in range(k_won, m + 1):
#         if dp[i - k_won] != sys.maxsize:
#             dp[i] = min(dp[i], dp[i - k_won] + 1)

# print(dp[m] if dp[m] != sys.maxsize else -1)

# 큰 화폐부터 빼주기
# n, m = map(int, input().split())
# unit_lst = [int(sys.stdin.readline()) for _ in range(n)]
# unit_lst.sort()
# count = 0

# while m:
#     for i in range(n-1, -1, -1):
#         if m - unit_lst[i] >=0:
#             m -= unit_lst[i]
#             count += 1
#             break
#         if i == 0:
#             print(-1)
#             sys.exit()
# print(count)

#######################################################################################################################

# 금광에서 캘 수 있는 최대 금 개수
# t = int(input())

# while t > 0:
#     n, m = map(int, sys.stdin.readline().split())
#     a = list(map(int, sys.stdin.readline().split()))
#     new_a = [[0] * m for _ in range(n)]
#     dp = [[0] * m for _ in range(n)]

#     for i in range(n):
#         new_a[i] = a[i * m:i * m + m]

#     for i in range(n):
#         dp[i][0] = new_a[i][0]

#     for j in range(1, m):
#         for i in range(n):
#             if 0 < i < n - 1:
#                 dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + new_a[i][j]
#             elif 0 < i:
#                 dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + new_a[i][j]
#             elif i < n - 1:
#                 dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + new_a[i][j]
    
#     for i in range(n):
#         print(dp[i])

#######################################################################################################################

