# 흐름 ex) 5개의 집에 3개의 공유기를 둘때
# 집과 집 사이의 최소간격은 1고정. 최대간격은 8이라 가정
# 1 ~ 8에 중간 값인 4부터 시작
# 공유기를 4m 간격으로 3개이상 둘 수 있음?
# y: 그러면 6m 간격으로 둬봐
# n: 그러면 2m 간격으로 둬봐

def func(arr, left, right):
    if left > right:
        return
    
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