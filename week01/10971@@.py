import sys

n = int(input())
w = [[0] * n for _ in range(n)]
result = sys.maxsize
visit = [0 for _ in range(n)]

for i in range(n):
    w[i] = list(map(int, input().split()))

def recursive(start, cur, cost, cnt):
    global result

    if cost > result:
        return
    
    if cnt == n:
        if w[cur][start]:
            cost += w[cur][start]
            if result > cost:
                result = cost
        return

    for i in range(n):
        if not visit[i] and w[cur][i]:
            visit[i] = 1
            recursive(start, i, cost + w[cur][i], cnt + 1)
            visit[i] = 0

for i in range(n):
    visit[i] = 1
    recursive(i, i, 0, 1)
    visit[i] = 0

print(result)