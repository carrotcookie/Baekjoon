import sys
import heapq
input = sys.stdin.readline

def find_root(p, x):

    def find_parent(p, x):
        if p[x] != x:
            p[x] = find_parent(p, p[x])
        return p[x]
    
    return find_parent(p, x)

def union_parent(p, a, b):
    a = find_root(p, a)
    b = find_root(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b

v, e = map(int, input().split())
p = [i for i in range(v + 1)]
graph = []
ans = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, (c, a, b))

for _ in range(e):
    cost, start, end = heapq.heappop(graph)

    # 확인용
    print(p[1:])

    if find_root(p, start) != find_root(p, end):
        union_parent(p, start, end)
        ans += cost

print(ans)