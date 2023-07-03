import sys
input = sys.stdin.readline

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, x, y):
    x = find_parent(p, x)
    y = find_parent(p, y)

    if x < y:
        p[y] = x
    else:
        p[x] = y

n = int(input())
m = int(input())
p = [i for i in range(n + 1)]
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key = lambda x: x[-1])
answer = 0
count = 0

for a, b, cost in edges:
    if find_parent(p, a) != find_parent(p, b):
        union_parent(p, a, b)
        answer += cost
        count += 1

        if count == n - 1:
            break

print(answer)