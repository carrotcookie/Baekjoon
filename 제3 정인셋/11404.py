import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = min(graph[start][end], cost)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != sys.maxsize:
            print(graph[i][j], end = ' ')
        else:
            print(0, end = ' ')
    print()