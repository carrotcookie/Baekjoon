# 숫자 들어오고 정렬 후 중간 인덱스 출력
import sys

def heapify_up_max(a):
    n = len(a)
    
    start = n - 1
    child = start
    tmp = a[start]

    while child > 0:
        parent = (child - 1) // 2

        if a[parent] >= tmp:
            break

        a[child] = a[parent]
        child = parent

    a[child] = tmp
def heapify_up_min(a):
    n = len(a)
    
    start = n - 1
    child = start
    tmp = a[start]

    while child > 0:
        parent = (child - 1) // 2

        if a[parent] <= tmp:
            break

        a[child] = a[parent]
        child = parent

    a[child] = tmp

def heapify_down_max(a):
    n = len(a)

    # if n == 0:
    #     return 

    start = 0
    parent = start
    tmp = a[start]

    while parent < n // 2:
        cl = parent * 2 + 1
        cr = cl + 1
        
        if cr > n-1:
            child = cl
        else:
            child = cr if a[cr] > a[cl] else cl

        if a[child] <= tmp:
            break

        a[parent] = a[child]
        parent = child

    a[parent] = tmp

def heapify_down_min(a):
    n = len(a)

    # if n == 0:
    #     return 

    start = 0
    parent = start
    tmp = a[start]

    while parent < n // 2:
        cl = parent * 2 + 1
        cr = cl + 1

        if cr > n-1:
            child = cl
        else:
            child = cl if a[cr] > a[cl] else cr

        if a[child] >= tmp:
            break

        a[parent] = a[child]
        parent = child

    a[parent] = tmp

left = []
right = []
result = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())

    if len(left) == len(right):
        left.append(x)
        heapify_up_max(left)
    else:
        right.append(x)
        heapify_up_min(right)

    if len(right) != 0 and left[0] > right[0]:
        left[0], right[0] = right[0], left[0]
        heapify_down_max(left)
        heapify_down_min(right)
    result.append(left[0])

    print(left[0])