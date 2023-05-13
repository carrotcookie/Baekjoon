# import sys
# input = sys.stdin.readline

# def sol(i, j):
#     global count

#     if i == x and j == y:
#         count += 1
#     if i > x or j > y:
#         return
    
#     for di, dj in direction:
#         ni, nj = i + di, j + dj

#         if ni < 1 or ni > h or nj < 1 or nj > w: continue

#         if not graph[ni][nj]:
#             graph[ni][nj] = 1
#             sol(ni, nj)
#             graph[ni][nj] = 0



# w, h = map(int, input().split())
# x, y = map(int, input().split())
# graph = [[0] * (w + 1) for _ in range(h + 1)]
# direction = [(1, 0), (0, 1)]
# count = 0

# graph[1][1] = 1
# sol(1, 1)

# print(count)

import sys
input = sys.stdin.readline

def dfs1(i, j):
    if i == y and j == x:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    for di, dj in direction:
        ni, nj = i + di, j + dj

        if ni > y or nj > x: continue

        dp[i][j] += dfs1(ni, nj)
    
    return dp[i][j]

def dfs2(i, j):
    if i == h and j == w:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    for di, dj in direction:
        ni, nj = i + di, j + dj

        if ni > h or nj > w: continue

        dp[i][j] += dfs2(ni, nj)
    
    return dp[i][j]

w, h = map(int, input().split())
x, y = map(int, input().split())
ans = 0

if x == 1 and y == 1:
    x, y = w, h

dp = [[-1] * (w + 1) for _ in range(h + 1)]
direction = [(1, 0), (0, 1)]

from_home_to_toast = dfs1(1, 1)
from_toast_to_school = dfs2(y, x)

if from_home_to_toast == 0:
    from_home_to_toast = 1
if from_toast_to_school == 0:
    from_toast_to_school = 1

print(from_home_to_toast * from_toast_to_school % 1000007)