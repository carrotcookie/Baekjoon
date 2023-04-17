import sys

def heapify_up():
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

def heapify_down():
    n = len(a)

    if n == 0:
        return 

    start = 0
    parent = start
    tmp = a[start]

    while parent < n // 2:
        cl = parent * 2 + 1
        cr = cl + 1
        child = cr if cr <= n-1 and a[cr] > a[cl] else cl

        if a[child] <= tmp:
            break

        a[parent] = a[child]
        parent = child

    a[parent] = tmp


a = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())

    if x:
        a.append(x)
        heapify_up()
    else:
        if not a:
            print(0)
            continue

        a[0], a[-1] = a[-1], a[0]
        print(a.pop())
        heapify_down()