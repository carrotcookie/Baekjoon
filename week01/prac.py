# from collections import deque

# def bfs(x, y):
#     queue.append((x, y))

#     while queue:
#         cx, cy = queue.popleft()
#         for dx, dy in dir:
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and a[nx][ny] == 0:
#                 visit[nx][ny] = 1
#                 queue.append((nx, ny))

# n, m = map(int, input().split())
# a = [[0] * m for _ in range(n)]
# visit = [[0] * m for _ in range(n)]
# dir = [(1,0), (-1,0), (0,1), (0,-1)]
# queue = deque()
# count = 0

# for i in range(n):
#     a[i] = list(map(int, input().split()))

# for x in range(n):
#     for y in range(m):
#         if not visit[x][y] and a[x][y] == 0:
#             visit[x][y] = 1
#             bfs(x, y)
#             count += 1
# print(count)

###########################################################################

import sys

# def dfs(x, y, count):
#     global result

#     if count >= result:
#         return
    
#     if x == n-1 and y == m-1:
#         print()
#         for i in range(n):
#             for j in range(m):
#                 print(f'{visit[i][j]:-2}', end=' ')
#             print()
#         print(f'\n정답: {visit[x][y]}번')
#         exit()

#     for dx, dy in dir:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and a[nx][ny] == 1:
#             visit[nx][ny] = visit[x][y] + 1
#             dfs(nx, ny, count + 1)

# n, m = map(int, input().split())
# visit = [[0] * m for _ in range(n)]
# dir = [(-1,0), (0,-1), (0,1), (1,0)]
# a = []
# result = sys.maxsize

# for _ in range(n):
#     a.append(list(map(int, input())))

# visit[0][0] = 1
# dfs(0, 0, 1)

from collections import deque

def bfs(x, y):
    visit[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            break

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and a[nx][ny] == 1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))
                
        


n, m = map(int, input().split())
visit = [[0] * m for _ in range(n)]
queue = deque()
dir = [(1,0), (-1,0), (0,1), (0,-1)]
a = []

for _ in range(n):
    a.append(list(map(int, input())))

bfs(0, 0)

for i in range(n):
    for j in range(m):
        print(f'{visit[i][j]:>2}', end=' ')
    print()