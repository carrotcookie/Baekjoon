import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(cur):
    # root인 1번 노드부터 시작
    for next_node in graph[cur]:
        # 자식의 부모 설정이 안되어있다면
        # 자식에게 자신번호 전달
        if not p[next_node]:
            p[next_node] = cur
            dfs(next_node)


n = int(input())
graph = [[] for _ in range(n + 1)]
p = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(*p[2:], sep = '\n')