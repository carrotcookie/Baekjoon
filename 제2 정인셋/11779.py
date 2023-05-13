import sys
import heapq
input = sys.stdin.readline

def dijkstar(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 목표 도시까지 왔으면 종료
        if now == end_city: return
        # 이미 처리되었으면 continue
        if distance[now] < dist: continue

        for i in graph[now]:
            next = i[0]
            cost = dist + i[1]

            if cost < distance[next]:
                distance[next] = cost
                # 가장 빠르게 next에 왔을 때 바로 전 도시 갱신
                path[next] = now
                heapq.heappush(q, (cost, next))

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [sys.maxsize] * (n + 1)
path = {i: 0 for i in range(n + 1)}

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start_city, end_city = map(int, input().split())
ans = [end_city]

dijkstar(start_city)

print(distance[end_city])
while end_city != start_city:
    ans.append(path[end_city])
    end_city = path[end_city]
print(len(ans))
print(*(ans[::-1]))