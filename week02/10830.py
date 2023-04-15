import sys

def mul(a1, a2):
    new_a = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            x = 0
            for k in range(n):
                x += a1[i][k] * a2[k][j]
            new_a[i][j] = x % 1000
    
    return new_a

def pow(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    
    tmp = pow(a, b // 2)

    if b % 2:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)

n, b = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for row in pow(arr, b):
    print(*row)