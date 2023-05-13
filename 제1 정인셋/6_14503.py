import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0

# 비어있지만 청소한 칸 2
# 막혀있는 칸 1
# 비어있고 청소안한 칸 0

while True:
    if not a[r][c]:
        a[r][c] = 2
        ans += 1
    
    for dx, dy in direction:
        nr, nc = r + dx, c + dy

        if not a[nr][nc]:
            d = d - 1 if d - 1 >= 0 else 3
            nnr = r + direction[d][0]
            nnc = c + direction[d][1]

            if not a[nnr][nnc]:
                r, c = nnr, nnc
                break

            break
    else:
        nr, nc = r - direction[d][0], c - direction[d][1]
        if a[nr][nc] != 1:
            r, c = nr, nc
        else:
            break

print(ans)