import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# 1. 다익스트라
# A노드에서 B노드까지 가는 최단거리

# # 방문하지 않은 노드 중, 최단 거리의 노드 번호 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n + 1):
#         if dist[i] < min_value and not visit[i]:
#             min_value = dist[i]
#             index = i
#     return index

# def dijkstra(start):
#     # 시작 노드 초기화
#     dist[start] = 0
#     visit[start] = True
#     for i in graph[start]:
#         # start에서 i[0]으로 가는데 드는 비용
#         dist[i[0]] = i[1]
#     for i in range(n - 1):
#         cur = get_smallest_node()
#         visit[cur] = True

#         for j in graph[cur]:
#             # 현재 노드까지의 최단거리에 다음노드까지의 거리를 더해줌
#             cost = dist[cur] + j[1]
#             # 현 상황에서 start에서 다음노드까지의 비용보다 cost가 작으면 갱신
#             if cost < dist[j[0]]:
#                 dist[j[0]] = cost

# # 노드 개수. 간선 개수
# n, m = map(int, input().split())
# # 시작 노드
# start = int(input())
# # 간선 정보
# graph = [[] for i in range(n + 1)]
# # 방문 리스트
# visit = [False] * (n + 1)
# # 최단 거리 테이블
# dist = [INF] * (n + 1)

# for _ in range(m):
#     # a -> b 로 가는 비용 c
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# dijkstra(start)

# for i in range(1, n + 1):
#     if dist[i] == INF:
#         print('INFINITY')
#     else:
#         print(dist[i])

#####################################################################################################################

# 2. 힙 다익스트라

# def dijkstra(start):
#     q = []
#     # 시작 노드 초기화
#     heapq.heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         # 비용이 가장 작은 노드
#         dist, cur = heapq.heappop(q)
#         # 이미 처리된 적 있는 노드는 무시
#         if distance[cur] < dist:
#             continue
#         for i in graph[cur]:
#             # 현재 노드까지의 최단거리에 다음노드까지의 거리를 더해줌
#             cost = dist + i[1]
#             # 현 상황에서 start에서 다음노드까지의 비용보다 cost가 작으면 갱신
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# # 노드 개수. 간선 개수
# n, m = map(int, input().split())
# # 시작 노드
# start = int(input())
# # 간선 정보
# graph = [[] for i in range(n + 1)]
# # 최단거리 테이블
# distance = [INF] * (n + 1)

# for _ in range(m):
#     # a -> b 로 가는 비용 c
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# dijkstra(start)

# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print('INFINITY')
#     else:
#         print(distance[i])

#####################################################################################################################

# 3. 플로이드 워셜
# 모든노드에서 다른노드까지 가는 최단거리
# 노드의 개수가 적은게 아닌이상 다익스트라 여러번 반복이 효율적 (보통 500개 이하)
# O(N^3)

# # 노드 개수, 간선 개수
# n, m = map(int, input().split())
# # 최단거리 테이블
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# # 자기 자신으로 가는 비용 0으로 초기화
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0

# for _ in range(m):
#     # a -> b 비용 c
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# # a -> b 비용을 a -> k -> b 처럼 k를 거쳐가는 비용과 비교하여 작은 값으로 갱신
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == INF:
#             print('INFINITY', end = ' ')
#         else:
#             print(graph[a][b], end = ' ')
#     print()

#####################################################################################################################

# 4. 서로소 집합 자료구조 (Union & Find)
# 루트 노드가 같은 노드끼리는 같은 집합임

# 현재 노드의 부모를 재귀적으로 찾아
# 최종적으로 루트 노드를 찾는다
def find_root(p, x):
    def find_parent(p, x):
        # 자기 노드의 부모가 자기 자신이 아니라면 루트 노드가 아니기 때문에
        # 루트 노드를 찾을 때까지 반복

        # 1. 비효율적
        # if p[x] != x:
        #     return find_parent(p, p[x])
        # return x

        # 2. 경로 압축
        # 한번 실행되고나면 타고타고 들어가서 찾는게 아닌
        # 바로 루트를 찾고 반환 받게 된다
        if p[x] != x:
            p[x] = find_parent(p, p[x])
        return p[x]    
    
    return find_parent(p, x)

# 두 노드를 같은 집합으로 처리하기
def union_parent(p, a, b):
    # 각자 자신의 노드의 루트 노드를 찾는다
    a = find_root(p, a)
    b = find_root(p, b)
    # 더 큰 루트노드를 가진쪽이 작은쪽을 부모로 삼는다
    if a < b:
        p[b] = a
    else:
        p[a] = b

#####################################################################################################################

# 5. 신장 트리 (MST)
# 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않아야 함
# 간선비용을 오름차순 정렬 후 작은거 부터 사이클이 존재 하지 않으면 포함시켜줌