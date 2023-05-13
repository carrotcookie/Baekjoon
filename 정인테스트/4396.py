# 틀린코드 수정 안할거임
# 틀린부분: 지뢰 밟았을 때 뒤쪽 인덱스 지뢰는 다 표시 되는데 앞쪽 인덱스 지뢰가 표시안됨

import sys
input = sys.stdin.readline

n = int(input())
mine_info = [input().rstrip() for _ in range(n)]
state_info = [input().rstrip() for _ in range(n)]
result = [['0'] * n for _ in range(n)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
gameover = False

for x in range(n):
    for y in range(n):
        if state_info[x][y] == 'x': 
            if mine_info[x][y] == '*':
                result[x][y] = '*'
                gameover = True
            else:
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1: continue
                    
                    if mine_info[nx][ny] == '*':
                        result[x][y] = str(int(result[x][y]) + 1)
        else:
            if gameover and mine_info[x][y] == '*':
                result[x][y] = '*'
                continue

            result[x][y] = '.'

for row in result:
    print(*row, sep = '')