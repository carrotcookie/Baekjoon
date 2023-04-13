import sys

def func(target, left, right):
    global result

    if left > right:
        return None
    
    cut_h = (left + right) // 2

    tmp = 0
    for x in arr:
        if x > cut_h:
            tmp += x - cut_h

    if tmp < target:
        func(target, left, cut_h - 1)
    else:
        result = cut_h
        func(target, cut_h + 1, right)

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
left, right = 0, max(arr)
result = 0

func(m, left, right)
print(result)