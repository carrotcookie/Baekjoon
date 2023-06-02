import sys
input = sys.stdin.readline

def find_like(info):
    count = 0

    for i in range(n):
        for j in range(n):
            if seat[i][j] == info[0]:
                for dx, dy in direction:
                    nx, ny = i + dx, j + dy

                    if 0 <= nx < n and 0 <= ny < n and seat[nx][ny] in info[1:]:
                        count += 1

                return count


n = int(input())
seat = [[0] * n for _ in range(n)]
relationships = [list(map(int, input().split())) for _ in range(n**2)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = 0

# 비어있으면 일단 앉혀놓고 조건들 기록
for relationship in relationships:
    tmp = []
    for i in range(n):
        for j in range(n):
            if seat[i][j] != 0: continue

            like_cnt = 0
            empty_cnt = 0

            for di, dj in direction:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < n:
                    if seat[ni][nj] == 0:
                        empty_cnt += 1
                    elif seat[ni][nj] in relationship[1:]:
                        like_cnt += 1

            tmp.append((like_cnt, empty_cnt, i, j))
    
    tmp.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    seat[tmp[0][2]][tmp[0][3]] = relationship[0]

for relationship in relationships:
    cnt = find_like(relationship)

    if cnt == 1:
        ans += 1
    elif cnt == 2:
        ans += 10
    elif cnt == 3:
        ans += 100
    elif cnt == 4:
        ans += 1000

print(ans)