import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 1991. 트리 순회
# def pre_order(parent):
#     if parent != '.':
#         print(parent, end = '')
#         pre_order(graph[parent][0])
#         pre_order(graph[parent][1])

# def in_order(parent):
#     if parent != '.':
#         in_order(graph[parent][0])
#         print(parent, end = '')
#         in_order(graph[parent][1])

# def post_order(parent):
#     if parent != '.':
#         post_order(graph[parent][0])
#         post_order(graph[parent][1])
#         print(parent, end = '')

# n = int(input())
# graph = {}

# for _ in range(n):
#     a, b, c = input().split()
#     graph[a] = [b, c]

# pre_order('A')
# print()
# in_order('A')
# print()
# post_order('A')

#####################################################################

# 5639. 이진 검색 트리
# sys.setrecursionlimit(10 ** 9)

# def post_order(start, end):
#     if start == end:
#         print(a[start])
#         return   
    
#     root = a[start]

#     # 나눌 영역이 1개 밖에 없을 때 미리 처리
#     if root < a[start + 1] or root > a[end]:
#         post_order(start + 1, end)
#         print(root)
#         return

#     # 나눌 영역이 2개일 때
#     # e.g. 50 / (30 24 5 28 45) (98 52 60)
#     # root는 50, root랑 비교해서 큰 값 나오는 순간 분할
#     for i in range(start + 2, end + 1):
#         if root < a[i]:
#             post_order(start + 1, i - 1)
#             post_order(i, end)
#             print(root)
#             return

# a = []

# while True:
#     try:
#         a.append(int(input()))
#     except:
#         break

# post_order(0, len(a) - 1)

#####################################################################

# 1197. 최소 스패닝 트리
# 크루스칼 알고리즘, Union Find (무방향 그래프 사이클 판별)
# 최소 가중치를 위해 간선을 오름차순 정렬
# 정렬된 간선 정보를 읽어오면서 사이클이 없을때에만 가중치를 누적
# def find_root(p, x):
#     def find_parent(p, x):
#         if p[x] != x:
#             return find_parent(p, p[x])
#         return x
    
#     return find_parent(p, x)

# def union_parent(p, a, b):
#     a = find_root(p, a)
#     b = find_root(p, b)

#     if a < b:
#         p[b] = a
#     else:
#         p[a] = b

# v, e = map(int, input().split())
# p = [i for i in range(v + 1)]
# graph = []
# ans = 0
# count = 0

# for _ in range(e):
#     a, b, c = map(int, input().split())
#     # 간선정보를 가중치에 대해 오름차순 정렬
#     heapq.heappush(graph, [c, a, b])

# for _ in range(e):
#     cost, start, end = heapq.heappop(graph)

#     if find_root(p, start) != find_root(p, end):
#         union_parent(p, start, end)
#         ans += cost
#         count += 1
#         # 간선이 v-1개가 되면 완료된거임 
#         if count == v - 1:
#             break

# print(ans)

#####################################################################

# 1260. DFS와 BFS
# def dfs(start):
#     visit_dfs[start] = 1
#     print(start, end = ' ')
    
#     for next in sorted(graph[start]):
#         if not visit_dfs[next]:
#             dfs(next)

# def bfs(start):
#     q = deque([start])
#     visit_bfs[start] = 1

#     while q:
#         now = q.popleft()
#         print(now, end = ' ')

#         for next in sorted(graph[now]):
#             if not visit_bfs[next]:
#                 visit_bfs[next] = 1
#                 q.append(next)


# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# visit_dfs = [0] * (n + 1)
# visit_bfs = [0] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# dfs(v)
# print()
# bfs(v)

#####################################################################

# 11724. 연결 요소의 개수
# def dfs(start):
#     visit[start] = 1

#     for next in graph[start]:
#         if not visit[next]:
#             dfs(next)

# def bfs(start):
#     q = deque()
#     visit[start] = 1
#     q.append(start)

#     while q:
#         now = q.popleft()

#         for next in graph[now]:
#             if not visit[next]:
#                 visit[next] = 1
#                 q.append(next)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# count = 0

# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# for i in range(1, n + 1):
#     if not visit[i]:
#         # dfs, bfs 택 1
#         # dfs(i)
#         bfs(i)
#         count += 1

# print(count)

#####################################################################

# 2606. 바이러스
# 1. dfs, bfs
# def dfs(start):
#     global count

#     visit[start] = 1

#     for next in graph[start]:
#         if not visit[next]:
#             count += 1
#             dfs(next)

# def bfs(start):
#     global count
#     q = deque()
#     visit[start] = 1
#     q.append(start)

#     while q:
#         now = q.popleft()

#         for next in graph[now]:
#             if not visit[next]:
#                 visit[next] = 1
#                 count += 1
#                 q.append(next)  

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# count = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # dfs, bfs 택 1
# # dfs(1)
# bfs(1)

# print(count)

# -----------------------------------------

# 2. 크루스칼
# def find_parent(p, x):
#     if p[x] != x:
#         p[x] = find_parent(p, p[x])
    
#     return p[x]

# def union_parent(p, a, b):
#     a = find_parent(p, a)
#     b = find_parent(p, b)

#     if a < b:
#         p[b] = a
#     else:
#         p[a] = b

# n = int(input())
# m = int(input())
# graph = []
# p = [i for i in range(n + 1)]
# count = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph.append([a, b])

# for info in graph:
#     a, b = info
#     union_parent(p, a, b)

# for i in range(1, n + 1):
#     find_parent(p, i)

# # 자기자신은 제외
# print(p.count(1) - 1)

#####################################################################

# 11725. 트리의 부모 찾기
# def dfs(start, parent):
#     visit_parent[start] = parent

#     for next in graph[start]:
#         if not visit_parent[next]:
#             dfs(next, start)

# def bfs(start, parent):
#     q = deque()
#     visit_parent[start] = parent
#     q.append(start)

#     while q:
#         now = q.popleft()

#         for next in graph[now]:
#             if not visit_parent[next]:
#                 visit_parent[next] = now
#                 q.append(next)

# n = int(input())
# graph = [[] for _ in range(n + 1)]
# visit_parent = [0] * (n + 1)

# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # dfs, bfs 택 1
# # dfs(1, 1)
# bfs(1, 1)
# print(*visit_parent[2:], sep = '\n')

#####################################################################

# 1707. 이분 그래프
# def dfs(start, symbol):
#     global success
#     visit[start] = symbol

#     for next in graph[start]:
#         if visit[next] == 0:
#             dfs(next, -symbol)
#         elif visit[next] == visit[start]:
#             success = False
#             return

# def bfs(start, symbol):
#     global success
#     q = deque()
#     visit[start] = symbol
#     q.append(start)

#     while q:
#         now = q.popleft()

#         for next in graph[now]:
#             if visit[next] == 0:
#                 visit[next] = -visit[now]
#                 q.append(next)
#             elif visit[next] == visit[now]:
#                 success = False
#                 return

# k = int(input())

# for _ in range(k):
#     v, e = map(int, input().split())
#     graph = [[] for _ in range(v + 1)]
#     visit = [0] * (v + 1)
#     success = True

#     for _ in range(e):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
    
#     for i in range(1, v + 1):
#         if visit[i] == 0:
#             # dfs, bfs 택 1
#             # dfs(i, 1)
#             bfs(i, 1)
#         if not success:
#             break

#     print('YES' if success else 'NO')

#####################################################################

# 21606. 아침 산책
# 1. 108점 시간초과 (실내기준)
# def dfs(start):
#     global count
#     visit[start] = 1

#     for next in graph[start]:
#         if not visit[next]:
#             # 실내만나면 카운팅
#             if a[next] == '1':
#                 count += 1
#             # 실외면 실내 만날때까지 더 들어가
#             else:
#                 dfs(next)
#                 visit[next] = 0
        
# n = int(input())
# a = '0' + input().rstrip()
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# count = 0

# for _ in range(n - 1):
#     u, v = map(int, input().split())

#     if a[u] == a[v] == 1:
#         count += 2
#         continue

#     graph[u].append(v)
#     graph[v].append(u)

# for i in range(1, n + 1):
#     # 실내일 때만 시작
#     if a[i] == '1':
#         dfs(i)
#         visit[i] = 0

# print(count)

# -----------------------------------------

# 2. 200점 실외기준
# 실외 관점에서 볼때는 카운팅 방식때문에
# 방문처리를 해제하면 안됨
# def dfs(start):
#     global tmp
#     visit[start] = 1

#     for next in graph[start]:
#         if not visit[next]:
#             # 실내만나면 카운팅
#             if a[next] == '1':
#                 tmp += 1
#             # 실외면 실내 만날때까지 더 들어가
#             else:
#                 dfs(next)
# def bfs(start):
#     global tmp
#     q = deque()
#     visit[start] = 1
#     q.append(start)

#     while q:
#         now = q.popleft()

#         for next in graph[now]:
#             if not visit[next]:
#                 if a[next] == '1':
#                     tmp += 1
#                 else:
#                     visit[next] = 1
#                     q.append(next)
        
# n = int(input())
# # 인덱스 1부터 쓰려고 '0' 더해준거임
# a = '0' + input().rstrip()
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# count = 0
# tmp = 0

# for _ in range(n - 1):
#     u, v = map(int, input().split())

#     # 이어진 두 노드가 실내라면 +2
#     # 간선 정보에 안넣어도 됨
#     if a[u] == a[v] == '1':
#         count += 2
#         continue

#     graph[u].append(v)
#     graph[v].append(u)

# for i in range(1, n + 1):
#     # 실외일 때만 시작
#     if not visit[i] and a[i] == '0':
#         # dfs, bfs 택 1
#         # dfs(i)
#         bfs(i)
#         # 실외 기준으로 실내가 n개 탐색되면
#         # nP2 만큼 추가됨
#         count += tmp * (tmp - 1)
#         tmp = 0

# print(count)

# -----------------------------------------

# 3. 위상정렬

#####################################################################

# 14888. 연산자 끼워넣기
# def func(idx, result, add, sub, mul, div):
#     global max_value
#     global min_value

#     if idx == n:
#         max_value = max(max_value, result)
#         min_value = min(min_value, result)
#         return
    
#     if add:
#         func(idx + 1, result + a[idx], add - 1, sub, mul, div)
#     if sub:
#         func(idx + 1, result - a[idx], add, sub - 1, mul, div)
#     if mul:
#         func(idx + 1, result * a[idx], add, sub, mul - 1, div)
#     if div:
#         # // 연산자 쓰면 음수를 양수로 나눌때 요구대로 안됨
#         func(idx + 1, int(result / a[idx]), add, sub, mul, div - 1)

# n = int(input())
# a = [int(x) for x in input().split()]
# add, sub, mul, div = map(int, input().split())
# max_value = -sys.maxsize
# min_value = sys.maxsize

# func(1, a[0], add, sub, mul, div)
# print(max_value)
# print(min_value)

#####################################################################

# 2573. 빙산
# def dfs(x, y):
#     visit[x][y] = 1

#     for dx, dy in dir:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#             continue
#         # 0 만나면 빼야할 개수 누적
#         if graph[nx][ny] == 0:
#             sub[x][y] += 1
#         # 탐색
#         elif not visit[nx][ny]:
#             dfs(nx, ny)
    
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visit = [[0] * m for _ in range(n)]
# sub = [[0] * m for _ in range(n)]
# ice_pos = deque()
# dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# ans = 0

# for i in range(n):
#     for j in range(m):
#         if graph[i][j]:
#             ice_pos.append((i, j))

# while ice_pos:
#     count = 0

#     # 탐색
#     for i, j in ice_pos:
#         if not visit[i][j]:
#             dfs(i, j)
#             count += 1

#     # 영역이 1개라면 빼야할 높이 만큼 빼준다
#     # sub, visit 0으로 다시 돌려놓음
#     # 영역의 높이가 아직 남아 있으면 pop했던 좌표 다시 append로 집어넣음
#     if count == 1:
#         k = len(ice_pos)

#         for _ in range(k):
#             i, j= ice_pos.popleft()
#             graph[i][j] -= sub[i][j]
#             sub[i][j] = 0
#             visit[i][j] = 0

#             if graph[i][j] <= 0:
#                 graph[i][j] = 0
#                 continue

#             ice_pos.append((i, j))
#     else:
#         break

#     ans += 1

# if ice_pos:
#     print(ans)
# else:
#     print(0)

#####################################################################

# 2617. 구슬 찾기
# 1. DFS
# def dfs(start, count, x):
#     visit[start] = 1
#     # x에 따라 작은쪽으로 탐색할건지 큰쪽으로 탐색할건지 정해짐
#     for next in graph[start][x]:
#         if not visit[next]:
#             # 자신보다 크거나 작은거 몇개인지 누적됨
#             count = dfs(next, count + 1, x)

#     return count

# n, m = map(int, input().split())
# graph = [[[] for _ in range(2)] for _ in range(n + 1)]
# ans = 0
# pivot = (n - 1) // 2

# for _ in range(m):
#     a, b = map(int, input().split())
#     # 자신보다 작으면 [0]에 추가
#     graph[a][0].append(b)
#     # 자신보다 크면 [1]에 추가
#     graph[b][1].append(a)

# for i in range(1, n + 1):
#     # 기준이 달라질 때마다 방문 초기화
#     visit = [0] * (n + 1)

#     if dfs(i, 0, 0) > pivot: 
#         ans += 1
#     if dfs(i, 0, 1) > pivot: 
#         ans += 1

# print(ans)

# 2. 플로이드 워셜
# n, m = map(int, input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# mid = n // 2
# ans = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1

# # 자신의 노드보다 가볍지만 직접 갈 수 없는. 즉, 나보다 가벼운 노드에서 갈 수 있는 더 가벼운 노드
# # 현재 노드에서 어떠한 노드를 거쳐서 갈 수 있다면 그 정보를 추가해준다.
# for k in range(1, n + 1):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if graph[i][k] and graph[k][j]:
#                 graph[i][j] = 1

# for i in range(1, n + 1):
#     heavy_cnt = 0
#     light_cnt = 0

#     for j in range(1, n + 1):
#         if i == j: continue
#         # i 구슬보다 무거운 구슬의 개수
#         if graph[i][j]:
#             heavy_cnt += 1
#         # i 구슬보다 가벼운 구슬의 개수
#         if graph[j][i]:
#             light_cnt += 1
#     # 개수가 절반을 넘으면 중간에 놓일 가능성이 없음
#     if heavy_cnt > mid or light_cnt > mid:
#         ans += 1

# print(ans)

#####################################################################

# 2178. 미로 탐색
# def bfs(x, y):
#     q = deque()
#     visit[x][y] = 1
#     q.append((x, y))

#     while q:
#         now_x, now_y = q.popleft()
#         for dx, dy in direction:
#             nx, ny = now_x + dx, now_y + dy
#             if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#                 pass
#             else:
#                 # 방문하지 않았고 길이 있을 때
#                 if not visit[nx][ny] and int(graph[nx][ny]):
#                     visit[nx][ny] = visit[now_x][now_y] + 1
#                     q.append((nx, ny))

# n, m = map(int, input().split())
# graph = [list(input()) for _ in range(n)]
# visit = [[0] * m for _ in range(n)]
# direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# bfs(0, 0)
# print(visit[n - 1][m - 1])

#####################################################################

# 18352. 특정 거리의 도시 찾기
# def bfs(start):
#     q = deque()
#     dist[start] = 0
#     q.append(start)

#     while q:
#         now = q.popleft()

#         # 거리가 존재한다는 자체가 방문 했다는거
#         for next in graph[now]:
#             if not dist[next]:
#                 dist[next] = dist[now] + 1
#                 q.append(next)


# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# dist = [0] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# bfs(x)
# # dist[x]는 반드시 0이어야 하는데 방문 유무로도 쓰다보니 나중에 바뀔수도 있어서 초기화
# # 맨 처음 초기 방문이 0으로 처리되어서 여길 다시 들어올 수도 있음
# dist[x] = 0

# # 최단거리 중 k 가 없다면 -1 출력
# if not dist.count(k):
#     print(-1)
# # 최단거리가 k 인 노드 오름차순 출력
# else:
#     for i in range(1, n + 1):
#         if dist[i] == k:
#             print(i)

#####################################################################

# 1916. 최소비용 구하기
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         dist, now = heapq.heappop(q)
#         # end_city 노드가 뽑히면 현재노드까지는 최단거리 완료된거임
#         if now == end_city:
#             print(dist)
#             return
#         # 방문 처리 끝나고 나서 우선순위 밀려나서 남아있는것들 처리
#         if distance[now] < dist:
#             continue

#         # 현재 노드까지의 거리에 다음 노드 까지의 거리를 더한것을
#         for i in graph[now]:
#             cost = dist + i[1]
#             # 비교하여 더 작으면 갱신
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# distance = [sys.maxsize] * (n + 1)

# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     graph[start].append((end, cost))

# start_city, end_city = map(int, input().split())
# dijkstra(start_city)

#####################################################################

# 2665. 미로만들기
# def bfs(x, y):
#     q = []
#     visit[x][y] = 1
#     # 부순 횟수를 최소힙으로
#     heapq.heappush(q, (0, x, y))

#     while q:
#         change, now_x, now_y = heapq.heappop(q)
#         # 도착지점에 도달하면 현재까지 부순 횟수 출력
#         if now_x == now_y == n - 1:
#             print(change)
#             break

#         for dx, dy in direction:
#             nx, ny = now_x + dx, now_y + dy
#             if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
#                 continue
#             if not visit[nx][ny]:
#                 visit[nx][ny] = 1

#                 # 부순 횟수를 최소힙으로 하였기 때문에 길대로 가는 것이 먼저 다 수행되고 나서야
#                 # 뚫고 들어감 -> 최소 비용으로 부수고 도착

#                 # 뚫렸다면 그냥 감
#                 if graph[nx][ny]:  
#                     heapq.heappush(q, (change, nx, ny))
#                 # 막혔다면 부수고 들어감
#                 else:
#                     heapq.heappush(q, (change + 1, nx, ny))

# n = int(input())
# graph = [list(map(int, input().rstrip())) for _ in range(n)]
# visit = [[0] * n for _ in range(n)]
# direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# bfs(0, 0)

# 미로보기
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 0:
#             print('{0:>3}'.format('■'), end = '')
#         else:
#             print(f'{graph[i][j]:>3}', end = '')
#     print()

#####################################################################

# 7569. 토마토
# def bfs():
#     while q:
#         z, x, y = q.popleft()

#         for dz, dx, dy in direction:
#             nz, nx, ny = z + dz, x + dx, y + dy
#             if nz < 0 or nz > h - 1 or nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#                 continue

#             # 현재 익는 토마토가 있는 위치의 값은
#             # day + 1 이다
#             if not visit[nz][nx][ny] and graph[nz][nx][ny] == 0:
#                     graph[nz][nx][ny] = graph[z][x][y] + 1
#                     visit[nz][nx][ny] = 1
#                     q.append((nz, nx, ny))

# m, n, h = map(int, input().split())
# graph = [[] for _ in range(h)]
# visit = [[[0] * m  for _ in range(n)] for _ in range(h)]
# direction = [(0, -1, 0), (0, 0, -1), (0, 1, 0), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]
# day = 0
# q = deque()

# for i in range(h):
#         for j in range(n):
#             graph[i].append(list(map(int, input().split())))

# # 1인 지점을 먼저 다 집어넣고 bfs를 돌려야 함
# # 안 그러면 양쪽에 1이 있다 가정할 때 가운데로 좁혀오면 3일이면 될걸
# # 한쪽에서만 먼저 bfs를 진행해주면 6일이 걸리기 때문
# for k in range(h):
#     for i in range(n):
#         for j in range(m):
#             if not visit[k][i][j] and graph[k][i][j] == 1:
#                 visit[k][i][j] = 1
#                 q.append((k, i, j))

# bfs()

# # 3중 for문 어떻게 탈출할지 몰라서 죄다 break 걸어줌
# for k in range(h):
#     for i in range(n):
#         for j in range(m):
#             # 익힐 수 있는건 다 익혔는데 0이 남아있다면 -1
#             if graph[k][i][j] == 0:
#                 day = -1
#                 break
#             # graph 인덱스중 가장 큰거 - 1 이 답임
#             day = max(day, graph[k][i][j] - 1)
#         if day == -1:
#             break
#     if day == -1:
#         break

# print(day)

#####################################################################

# 3055. 탈출
# def bfs(start_x, start_y, end_x, end_y):
#     visit[start_x][start_y] = 1
#     # 시작지점을 제일 먼저 시작하기 위해 캐싱 해뒀다가 맨 앞으로 넣어줌
#     q.appendleft((start_x, start_y))

#     while q:
#         now_x, now_y = q.popleft()

#         # 도착지점에 고슴도치가 있으면 <- 이런식으로 판단해야함
#         # 현재 위치가 도착지점이면 <- 이렇게 판단하면 이미 고슴도치가 도착했어도 스택에 남아있는걸 처리하느라 거리저장값이 달라질 수 있음
#         # e.g. 이미 도착했어도 내 옆이 바로 물이 있고 해당 물을 처리할 차례이면 내 거리가 1로 바뀜
#         if graph[end_x][end_y] == 'S':
#             # 방문 처리와 거리를 동시에 쓰려고 첫 시작지점을 1로 했기 때문에 1을 빼줌
#             return visit[end_x][end_y] - 1

#         for dx, dy in direction:
#             nx, ny = now_x + dx, now_y + dy
#             if 0 <= nx < r and 0 <= ny < c:
#                 # 고슴도치는 . 또는 D 로만 나아감
#                 if not visit[nx][ny] and (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[now_x][now_y] == 'S':
#                     graph[nx][ny] = 'S'
#                     visit[nx][ny] = visit[now_x][now_y] + 1
#                     q.append((nx, ny))
#                 # 물은 . 또는 S 로만 나아감
#                 elif (graph[nx][ny] == 'S' or graph[nx][ny] == '.') and graph[now_x][now_y] == '*':
#                     graph[nx][ny] = '*'
#                     visit[nx][ny] = 1
#                     q.append((nx, ny))

#     return 'KAKTUS'


# r, c = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(r)]
# visit = [[0] * c for _ in range(r)]
# direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# q = deque()
# start_x, start_y = 0, 0
# end_x, end_y = 0, 0

# for i in range(r):
#     for j in range(c):
#         if graph[i][j] == '*':
#             q.append((i, j))
#         elif graph[i][j] == 'S':
#             start_x, start_y = i, j
#         elif graph[i][j] == 'D':
#             end_x, end_y = i, j

# print(bfs(start_x, start_y, end_x, end_y))

#####################################################################

# 2294. 동전 2
# 1. dp
# n, k = map(int, input().split())
# dp = [sys.maxsize] * (k + 1)
# dp[0] = 0

# for _ in range(n):
#     coin = int(input())

#     # 단위가 coin인 동전은 coin원 부터 낼 수 있기 때문
#     # 최종금액까지 반복해준다.
#     for i in range(coin, k + 1):
#         if dp[i - coin] != sys.maxsize:
#             dp[i] = min(dp[i], dp[i - coin] + 1)

# print(dp[k] if dp[k] != sys.maxsize else -1)

# -----------------------------------------

# 2. bfs
# def bfs():
#     q = deque()
#     coins = []

#     for _ in range(n):
#         tmp = int(input())
#         if tmp > k: continue

#         # 가치가 같은 동전 여러번 주어질 수도 있음
#         if tmp not in coins:
#             dp[tmp] = 1
#             q.append((tmp, dp[tmp]))
#             coins.append(tmp)

#     coins.sort()

#     while q:
#         k_won, cnt = q.popleft()

#         if k_won == k:
#             break

#         for coin in coins:
#             # sort를 해줬으면 break 안해줬으면 continue
#             if k_won + coin > k:
#                 break
#             # 이미 처리했는데 또 하면 괜히 1만 증가하게 되는꼴
#             if dp[k_won + coin] != 0:
#                 continue
#             # 원래 k_won 내는법 cnt, coin 내는법 1 -> cnt + 1
#             dp[k_won + coin] = cnt + 1
#             q.append((k_won + coin, cnt + 1))
    
#     return dp[k] if dp[k] else -1
        
# n, k = map(int, input().split())
# dp = [0] * (k + 1)
# dp[0] = 0

# print(bfs())

#####################################################################

# 2252. 줄 세우기
# def topology_sort():
#     result = []
#     q = deque()

#     for i in range(1, n + 1):
#         if in_count[i] == 0:
#             q.append(i)

#     while q:
#         now = q.popleft()
#         result.append(now)

#         for i in graph[now]:
#             in_count[i] -= 1
#             if in_count[i] == 0:
#                 q.append(i)
    
#     print(*result, sep = ' ')

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# in_count = [0] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     in_count[b] += 1

# topology_sort()

#####################################################################

# 2637. 장난감 조립
# 1. 시간초과
# def dfs(start, count):
#     if graph[start]:
#         for info in graph[start]:
#             node, cost = info
#             dfs(node, count * cost)
#     else:
#         result[start] += count

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# result = [0] * (n + 1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append([b, c])

# dfs(n, 1)

# for i in range(1, n + 1):
#     if result[i] != 0:
#         print(i, result[i])

# -----------------------------------------

# 2. 위상정렬
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n + 1)]
# needs = [[0] * (n + 1) for _ in range(n + 1)]
# in_degree = [0] * (n + 1)
# q = deque()

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[b].append([a, c])
#     in_degree[a] += 1

# for i in range(1, n + 1):
#     if in_degree[i] == 0:
#         q.append(i)

# while q:
#     now = q.popleft()

#     for next, cost in graph[now]:
#         # 기본부품
#         if needs[now][1:].count(0) == n:
#             # next 부품은 now 부품을 cost만큼 필요로 한다
#             needs[next][now] += cost
#         # 중간부품
#         else:
#             # next 부품은 now 부품의 각 요소를 가중치만큼 곱해서 갖는다
#             for i in range(1, n + 1):
#                 needs[next][i] += needs[now][i] * cost

#         in_degree[next] -= 1
#         if in_degree[next] == 0:
#             q.append(next)

# for i in range(1, n + 1):
#     if needs[n][i] != 0:
#         print(i, needs[n][i])

#####################################################################

