# import sys

# def func(target, left, right):
#     global result

#     if left > right:
#         return
    
#     cut_h = (left + right) // 2

#     tmp = 0
#     for x in arr:
#         if x > cut_h:
#             tmp += x - cut_h

#     if tmp < target:
#         func(target, left, cut_h - 1)
#     elif tmp == target:
#         result = cut_h
#         return
#     else:
#         result = cut_h
#         func(target, cut_h + 1, right)

# n, m = map(int, input().split())
# arr = list(map(int, sys.stdin.readline().split()))
# left, right = 0, max(arr)
# result = 0

# func(m, left, right)
# print(result)

#########################################################

import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(N_list)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in N_list:
        if i > mid:
            cnt += (i - mid)

    print(start, mid, end, cnt)

    if cnt > M: # 충분
        print('충분')
        start = mid + 1
    elif cnt == M:  
        print('딱')
        result = mid
        break
    else: #부족
        print('부족')
        end = mid - 1
        result = mid - 1

print()
print(mid)