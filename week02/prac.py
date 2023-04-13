# def binary_search(arr, target, left, right):
#     if left > right:
#         return None
    
#     mid = (left + right) // 2

#     if target == arr[mid]:
#         return mid
#     elif target < arr[mid]: # 왼쪽에 있으면
#         return binary_search(arr, target, left, mid - 1)
#     else:                   # 오른쪽에 있으면
#         return binary_search(arr, target, mid + 1, right)

# target = int(input())
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = binary_search(arr, target, 0, len(arr) - 1)

# if result:
#     print(f'{arr[result]}은 {result + 1}번째 원소입니다')
# else:
#     print('원소가 존재하지 않습니다.')

import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
left, right = 0, max(arr)

while left <= right:
    total = 0
    mid = (left + right) // 2

    for i in arr:
        if i > mid:
            total += i - mid

    if total < m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1
        

print(result)