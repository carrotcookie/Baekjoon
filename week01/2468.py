import sys

def recursive(i, j, h):
    tmp = []
    tmp.append((i, j))

    while len(tmp):
        i, j = tmp.pop()

        for dx, dy in dir:
            nx, ny = i + dx, j + dy

            if 0 <= nx and nx < n and 0 <= ny and ny < n and not visit[nx][ny] and a[nx][ny] > h:
                visit[nx][ny] = 1
                tmp.append((nx, ny))
    
    # recursionError 떠서 depth 강제로 늘려야함, default: 1000번
    # sys.setrecursionlimit(10 ** 6)
    # for dx, dy in dir:
    #     nx, ny = i + dx, j + dy
    #     if 0 <= nx and nx < n and 0 <= ny and ny < n and not visit[nx][ny] and a[nx][ny] > h:
    #         visit[nx][ny] = 1
    #         recursive(nx, ny, h)

dir = ((1,0), (-1,0), (0,-1), (0,1))
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

result = -sys.maxsize

for h in range(100): # 물 높이
    count = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and a[i][j] > h:
                visit[i][j] = 1
                recursive(i, j, h)
                count += 1

    result = max(result, count)
print(result)