import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

# 1. union & find

# def find_root(p, x):
#     def find_parent(p, x):
#         if p[x] != x:
#             p[x] = find_parent(p, p[x])
#         return p[x]
    
#     return find_parent(p, x)

# def union_parent(p, a, b):
#     a = find_root(p, a)
#     b = find_root(p, b)

#     if a < b:
#         p[b] = a
#     else:
#         p[a] = b

# n, m = map(int, input().split())
# p = [i for i in range(n + 1)]

# # 연결된 노드를 같은 루트로 묶어줌
# for _ in range(m):
#     a, b = map(int, input().split())
#     union_parent(p, a, b)

# # 갱신 안된 부분 때문에 1사이클 돌리는게 낭비인듯...
# for i in range(1, n + 1):
#     find_root(p, i)

# print(len(set(p[1:])))

######################################################################################################################

# 2. dfs

def dfs(cur, symbol):
    for next_node in graph[cur]:
        if not visit[next_node]:
            visit[next_node] = symbol
            dfs(next_node, symbol)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# visit = [i for i in range(n + 1)]
visit = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visit[i]:
        for next_node in graph[i]:
            if not visit[next_node]:
                visit[next_node] = i
                dfs(next_node, i)

bonus = visit[1:].count(0)
if bonus:
    bonus -= 1
else:
    bonus = 0

print(len(set(visit[1:])) + bonus)