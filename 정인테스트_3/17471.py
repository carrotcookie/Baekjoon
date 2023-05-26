import sys
from collections import deque
input = sys.stdin.readline

def combination(start, depth, dest):
    global tmp
    global ans

    if depth == dest:
        area1 = tmp
        area2 = [i for i in range(1, n + 1) if i not in tmp]

        popul_cnt1, visit_cnt1 = bfs(area1)
        popul_cnt2, visit_cnt2 = bfs(area2)

        if visit_cnt1 + visit_cnt2 == n:
            ans = min(ans, abs(popul_cnt1 - popul_cnt2))

        return
    
    for i in range(start, n + 1):
        tmp.append(i)
        combination(i + 1, depth + 1, dest)
        tmp.pop()

def bfs(div):
    q = deque([div[0]])
    visit_node = [div[0]]
    sum = 0
    length = 1

    while q:
        now = q.popleft()
        sum += population[now]

        for next in graph[now]:
            if next in div and next not in visit_node:
                q.append(next)
                visit_node.append(next)
                length += 1
    
    return [sum, length]
    

n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
ans = sys.maxsize

for i in range(1, n + 1):
    edge = list(map(int, input().split()))

    for neighbor in edge[1:]:
        graph[i].append(neighbor)

for cnt in range(1, n):
    tmp = []
    combination(1, 0, cnt)

print(ans if ans != sys.maxsize else -1)