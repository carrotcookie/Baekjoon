# 1. 시간초과
# import sys

# def func(left, right):
#     result = 0

#     if left > right: return result

#     mid = (left + right) // 2
#     max_count = 0
#     count = 0

#     for i in range(1, arr[0] + 1):
#         if arr[i] >= mid:
#             count += 1
#             if count > max_count:
#                 max_count = count
#         else:
#             count = 0

#     result = max(result, max_count * mid)

#     tmp1 = func(left, mid - 1)
#     tmp2 = func(mid + 1, right)

#     return  max(tmp1, tmp2, result)

# while True:
#     arr = list(map(int, sys.stdin.readline().split()))
#     if arr[0] == 0: exit()
#     left, right = 1, max(arr[1:])

#     print(func(left, right))

#################################################################################################

# 2. 스택
# import sys

# while True:
#     input = list(map(int, sys.stdin.readline().split()))
#     n = input[0]
#     arr = input[1:]
#     if n == 0: sys.exit()

#     stack = []
#     result = 0

#     for i in range(n):
#         width = 0

#         while stack and stack[-1][0] > arr[i]:
#             width += stack[-1][1]
#             result = max(result, width * stack[-1][0])
#             stack.pop()
        
#         width += 1
#         stack.append((arr[i], width))

#     width = 0
#     while stack:
#         width += stack[-1][1]
#         result = max(result, width * stack[-1][0])
#         stack.pop()

#     print(result)

#################################################################################################

# 3. 분할
import sys

def func(left, right):
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2

    result_l = func(left, mid)
    result_r = func(mid + 1, right)

    i = mid
    j = mid + 1
    w = 2
    h = min(arr[i], arr[j])
    result_m = 2 * h

    while left < i or j < right:

        if j < right and (left == i or arr[i - 1] < arr[j + 1]):
            j += 1
            w += 1
            h = min(h, arr[j])
        else:
            i -= 1
            w += 1
            h = min(h, arr[i])
        result_m = max(result_m, w * h)

    return max(result_l, result_m, result_r)


while True:
    input = list(map(int, sys.stdin.readline().split()))
    n = input[0]
    arr = input[1:]
    if n == 0: sys.exit()

    print(func(0, n - 1))