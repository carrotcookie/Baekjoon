import sys

def search(arr, target, left, right):
    if left > right:
        return 0
    
    mid = (left + right) // 2

    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return search(arr, target, mid + 1, right)
    else:
        return search(arr, target, left, mid - 1) 

n = int(input())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_arr = list(map(int, sys.stdin.readline().split()))

n_arr.sort()

for target in m_arr:
    print(search(n_arr, target, 0, n - 1))