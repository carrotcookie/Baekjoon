import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(x, y):
    global cnt

    a[x][y] = 0
    cnt += 1

    for dx, dy in direction:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and a[nx][ny]:
            dfs(nx, ny)

n, m, k = map(int, input().split())
a = [[0] * m for _ in range(n)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = 0

for _ in range(k):
    r, c = map(int, input().split())
    a[r - 1][c - 1] = 1

for i in range(n):
    for j in range(m):
        if a[i][j]:
            cnt = 0
            dfs(i, j)
            ans = max(ans, cnt)
    
print(ans)