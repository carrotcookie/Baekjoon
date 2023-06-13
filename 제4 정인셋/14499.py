import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
a = []
dice = [[0, 0], [0, 0], [0, 0]]
bottom_r, bottom_c = 0, 0
direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

orders = list(map(int, input().split()))

for order in orders:
    dx, dy = direction[order]
    nx, ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny

        if order == 1:
            bottom_r += 2
            if bottom_r > 2:
                bottom_r %= 3
        elif order == 2:
            bottom_r += 2
            bottom_c += 1
            if bottom_r > 2:
                bottom_r %= 3
            if bottom_c == 2:
                bottom_c = 0
        elif order == 3:
            bottom_r += 1
            if bottom_r > 2:
                bottom_r %= 3
        elif order == 4:
            bottom_r += 1
            bottom_c += 1
            if bottom_r > 2:
                bottom_r %= 3
            if bottom_c == 2:
                bottom_c = 0

        if a[x][y]:
            dice[bottom_r][bottom_c] = a[x][y]
            a[x][y] = 0
        else:
            a[x][y] = dice[bottom_r][bottom_c]
        
        if bottom_c == 0:
            print(dice[bottom_r][1])
        elif bottom_c == 1:
            print(dice[bottom_r][0])