import sys

n = int(input())
a = list(map(int, input().split()))
p = []
result = -sys.maxsize

def recursive(tmp):
    if len(tmp) == n:
        p.append(tmp[:])
        return

    for i in range(n):
        if i not in tmp:
            tmp.append(i)
            recursive(tmp)
            tmp.pop()

recursive([])

for i in range(len(p)):
    sum = 0
    for j in range(n - 1):
        sum += abs(a[p[i][j]] - a[p[i][j+1]])
    if result < sum:
        result = sum

print(result)