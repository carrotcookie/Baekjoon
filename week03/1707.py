import sys
input = sys.stdin.readline

def dfs(x, symbol):
    global flag

    flag[x] = symbol

    for i in graph[x]:
        if not flag[i]:
            dfs(i, -symbol)
        else:
            if flag[i] == symbol:
                print('NO')
                return

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    flag = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs(1, 1)