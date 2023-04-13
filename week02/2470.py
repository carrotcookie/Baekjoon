# 나만의 생각
# import sys

# def func(left, right):
#     n = len(abs_arr)

#     global result1
#     global result2

#     # 반복.
#     while left < right:

#         mid = (left + right) // 2
#         count = 0

#         for abs_sum, val1, val2 in abs_arr:
#             if abs_sum < mid:
#                 count += 1
#                 result1, result2 = val1, val2
#                 # print(f'합의 절대값이 {mid:3} 이하인거 {arr[result1]:3} {arr[result2]:3}')

#         if count:
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     #######################################################################################

#     # 재귀.
#     # if left > right:
#     #     return
    
#     # mid = (left + right) // 2
#     # count = 0

#     # for i in range(len(abs_arr)):
#     #     if abs_arr[i][0] < mid:
#     #         global result1
#     #         global result2

#     #         count += 1
#     #         result1 = abs_arr[i][1]
#     #         result2 = abs_arr[i][2]
#     #         print(f'합의 절대값이 {mid:3} 이하인거 {arr[result1]:3} {arr[result2]:3}')

#     # if count >= 1:
#     #     func(left, mid - 1)
#     # else:
#     #     func(mid + 1, right)

# n = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
# abs_arr = []
# arr.sort()

# for i in range(n):
#     for j in range(i+1, n):
#         abs_arr.append((abs(arr[i] + arr[j]), i, j))

# result1 = result2 = 0
# minimum = arr[0] + arr[1]
# maximum = arr[-1] + arr[-2]
# right = -minimum if abs(minimum) > maximum else maximum

# func(0, right)
# print(arr[result1], arr[result2])

##########################################################################################################################

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

pl, pr = 0, n - 1
tmp = sys.maxsize
result = [0, 0]

while pl < pr:
    sum = arr[pl] + arr[pr]

    if abs(sum) < tmp:
        tmp = abs(sum)
        result[0], result[1] = arr[pl], arr[pr]

    if sum < 0:
        pl += 1
    else:
        pr -= 1

print(result[0], result[1])