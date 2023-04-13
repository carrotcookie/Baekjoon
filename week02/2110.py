def func(arr, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    start_val = arr[0]
    count = 1

    for i in range(1, n):
        if arr[i] >= start_val + mid:
            count += 1
            start_val = arr[i]

    if count >= c:
        global result
        result = mid
        func(arr, mid + 1, right)
    else:
        func(arr, left, mid - 1)

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
result = 0
arr.sort()

left = 1
right = arr[-1] - arr[0]
func(arr, left, right)
print(result)