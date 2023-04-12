import sys

n = int(input())
a = [[0] * n for _ in range(n)]
visit = [0] * n
result = sys.maxsize

for i in range(n):
    tmp = list(map(int, input().split()))
    a[i] = tmp

def recursive(start, end, cost):
    global result 

    if cost > result:
        return
    
    if visit.count(1) == n:
        if a[start][end]:
            cost += a[start][end]
            if result > cost:
                result = cost
        return
    
    for j in range(n):
        if a[start][j] and not visit[j]:
            visit[j] = 1
            recursive(j, end, cost + a[start][j])
            visit[j] = 0

for i in range(n):
    visit[i] = 1
    recursive(i, i, 0)
    visit[i] = 0

print(result)