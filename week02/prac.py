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

a = [1, 2, 2, 2, 3, 5, 6, 7, 7]

while True:
    n = int(input())

    left = 0
    right = len(a) - 1
    result_idx = -1

    while left <= right:
        mid = (left + right) // 2

        # # 같은 값이 있다면 왼쪽
        if a[mid] >= n: 
            right = mid - 1
            result_idx = mid
        else:
            left = mid + 1
            result_idx = mid + 1

        # # 같은 값이 있다면 오른쪽
        # if a[mid] > n: 
        #     right = mid - 1
        #     result_idx = mid
        # else:
        #     left = mid + 1
        #     result_idx = mid + 1


    if result_idx > -1:
        print(f'{n}은 {a}에서 [{result_idx}]에 넣을 수 있습니다.')
    else:
        print(f'{n}은 {a}에 존재하지 않습니다.')