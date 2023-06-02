import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
ans = sys.maxsize

# e.g. n, m = 8이면 1번만 시도 가능.
for x in range(n - 7):
    for y in range(m - 7):
        w_start = 0
        b_start = 0

        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] == 'W':
                        b_start += 1
                    elif board[i][j] == 'B':
                        w_start += 1
                else:
                    if board[i][j] == 'W':
                        w_start += 1
                    elif board[i][j] == 'B':
                        b_start += 1
        
        ans = min(ans, min(w_start, b_start))

print(ans)