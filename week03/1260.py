import sys
from collections import deque
input = sys.stdin.readline

def dfs(cur):
    visit[cur] = 1
    print(cur, end = ' ')
    for i in range(1, n + 1):
        if not visit[i] and graph[cur][i]:
            dfs(i)
        
def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = 1

    while queue:
        cur = queue.popleft()
        print(cur, end = ' ')
        for i in range(1, n + 1):
            if not visit[i] and graph[cur][i]:
                queue.append(i)
                visit[i] = 1

n, m, v = map(int, input().split())
visit = [0] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
visit = [0] * (n + 1)
print()
bfs(v)