import sys
input = sys.stdin.readline

def check_a():
    print()
    for i in range(r):
        for j in range(c):
            print(f'{a[i][j]:>3}', end = '')
        print()

def on_cleaner():
    # 반시계 옮기기
    x, y = cleaner_row[0], 1
    tmp = 0
    before = 0
    while x != cleaner_row[0] or y != 0:
        tmp = a[x][y]
        a[x][y] = before
        before = tmp

        if x == cleaner_row[0]:
            if y != c - 1:
                y += 1
            else:
                x -= 1
        elif y == c - 1:
            if x != 0:
                x -= 1
            else:
                y -= 1
        elif x == 0:
            if y != 0:
                y -= 1
            else:
                x += 1
        else:
            x += 1
    
    # 시계 옮기기
    x, y = cleaner_row[1], 1
    tmp = 0
    before = 0
    while x != cleaner_row[1] or y != 0:
        tmp = a[x][y]
        a[x][y] = before
        before = tmp

        if x == cleaner_row[1]:
            if y != c - 1:
                y += 1
            else:
                x += 1
        elif y == c - 1:
            if x != r - 1:
                x += 1
            else:
                y -= 1
        elif x == r - 1:
            if y != 0:
                y -= 1
            else:
                x -= 1
        else:
            x -= 1

def dust_diffuse():
    # 확산된 미세먼지는 확산이 끝나고 나서 더해줄거임
    post_add_info = []

    # 확산 정보 추출
    for x in range(r):
        for y in range(c):
            if a[x][y] > 0:
                count = 0
                diffuse_amount = a[x][y] // 5

                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx > r - 1 or ny < 0 or ny > c - 1 or a[nx][ny] == -1: continue

                    post_add_info.append((nx, ny, diffuse_amount))
                    count += 1
                
                a[x][y] -= diffuse_amount * count

    # 확산
    for x, y, diffuse_amount in post_add_info:
        a[x][y] += diffuse_amount
    
    on_cleaner()

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
cleaner_row = []
ans = 0

for i in range(r):
    for j in range(c):
        if a[i][j] < 0:
            cleaner_row.append(i)

for _ in range(t):
    dust_diffuse()

for i in range(r):
    for j in range(c):
        if a[i][j] > 0:
            ans += a[i][j]

check_a()

print(ans)