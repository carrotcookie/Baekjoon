import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 2644. 촌수계산
# def dfs(start, depth):
#     global ans

#     visit[start] = 1
    
#     if start == target2:
#         ans = depth
#         return

#     for next in graph[start]:
#         if not visit[next]:
#             dfs(next, depth + 1)


# n = int(input())
# target1, target2 = map(int, input().split())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# ans = 0

# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# dfs(target1, 0)
# print(ans if ans else -1)

############################################################################################################################

# 23296. 엘리베이터 조작
# def bfs(start):
#     heap = []
#     heapq.heappush(heap, (0, start, 1))

#     while heap:
#         cnt, now, visit = heapq.heappop(heap)
#         next = graph[now]

    

# n = int(input())
# graph = ['dummy'] + list(map(int, input().split()))

# bfs(start)

############################################################################################################################

# 27653. 최소 트리 분할

############################################################################################################################

# 1012. 유기농 배추
# def bfs(r, c):
#     q = deque()
#     visit[r][c] = 1
#     q.append((r, c))

#     while q:
#         now_x, now_y = q.popleft()

#         for dx, dy in direction:
#             nx, ny = now_x + dx, now_y + dy
#             if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#                 continue
#             if not visit[nx][ny] and graph[nx][ny]:
#                 visit[nx][ny] = 1
#                 q.append((nx, ny))


# t = int(input())
# direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# for _ in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#     visit = [[0] * m for _ in range(n)]
#     q = deque()
#     count = 0

#     for _ in range(k):
#         x, y = map(int, input().split())
#         graph[y][x] = 1

#     for i in range(n):
#         for j in range(m):
#             if not visit[i][j] and graph[i][j]:
#                 bfs(i, j)
#                 count += 1

#     print(count)

############################################################################################################################

# 17086. 아기 상어 2
# def bfs():
#     while q:
#         now_x, now_y = q.popleft()

#         for dx, dy in direction:
#             nx, ny = now_x + dx, now_y + dy
#             if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#                 continue
#             if not visit[nx][ny] and not graph[nx][ny]:
#                 visit[nx][ny] = visit[now_x][now_y] + 1
#                 q.append((nx, ny))

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visit = [[0] * m for _ in range(n)]
# direction = [(-1,0), (0,-1), (1,0), (0,1), (-1,-1), (1,1), (1,-1), (-1,1)]
# q = deque()
# ans = 0

# for i in range(n):
#     for j in range(m):
#         if graph[i][j]:
#             visit[i][j] = 1
#             q.append((i, j))
# bfs()

# for i in range(n):
#     for j in range(m):
#         ans = max(ans, visit[i][j])
# print(ans - 1)

############################################################################################################################

# 13913. 숨바꼭질 4
def func(x):
    q = deque()
    q.append((x, [x]))

    while q:
        now, order = q.popleft()

        if now == k:
            return order
        
        n1 = now * 2
        n2 = now - 1
        n3 = now + 1

        if k // 2 <= n1 <= k * 2:
            lst1 = order + [n1]
            q.append((n1, lst1))
        if k // 2 <= n2 <= k * 2:
            lst2 = order + [n2]
            q.append((n2, lst2))
        if k // 2 <= n3 <= k * 2:
            lst3 = order + [n3]
            q.append((n3, lst3))

n, k = map(int, input().split())
result = func(n)
print(len(result) - 1)
print(*result)