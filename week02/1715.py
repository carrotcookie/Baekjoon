import sys

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

def heapify_down_min(a):
    n = len(a)

    if n == 0:
        return 

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

n = int(input())
a = []
ans = 0

if n == 1:
    int(input())
    print(0)
    sys.exit()
if n == 2:
    print(int(input()) + int(input()))
    sys.exit()

for _ in range(n):
    a.append(int(sys.stdin.readline()))
    heapify_up_min(a)

while n > 1:
    a[0], a[-1] = a[-1], a[0]
    n1 = a.pop()
    heapify_down_min(a)

    a[0], a[-1] = a[-1], a[0]
    n2 = a.pop()
    heapify_down_min(a)

    tmp = n1 + n2
    a.append(tmp)
    heapify_up_min(a)

    ans += tmp
    n -= 1

print(ans)