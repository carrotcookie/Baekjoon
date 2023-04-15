import sys

def func(a, n, x, y, no_cnt, color):
    if n == 0:
        return

    is_full = True

    if not color:
        if not no_cnt:
            for i in range(x-n, x):
                for j in range(y-n, y):
                    if a[i][j] == 1:
                        is_full = False
                        break

            if is_full:
                global cnt_white
                cnt_white += 1
                # print(f'크기 {n}일 때 [{x - n + 1}, {x}] // [{y - n + 1}, {y}]')

        # 1사분면
        func(a, n//2, x - n//2, y - n//2, is_full, 0)
        # 2사분면
        func(a, n//2, x - n//2, y, is_full, 0)
        # 3사분면
        func(a, n//2, x, y - n//2, is_full, 0)
        # 4사분면
        func(a, n//2, x, y, is_full, 0)
    else:
        if not no_cnt:
            for i in range(x-n, x):
                for j in range(y-n, y):
                    if a[i][j] == 0:
                        is_full = False
                        break

            if is_full:
                global cnt_blue
                cnt_blue += 1
                # print(f'크기 {n}일 때 [{x - n + 1}, {x}] // [{y - n + 1}, {y}]')

        # 1사분면
        func(a, n//2, x - n//2, y - n//2, is_full, 1)
        # 2사분면
        func(a, n//2, x - n//2, y, is_full, 1)
        # 3사분면
        func(a, n//2, x, y - n//2, is_full, 1)
        # 4사분면
        func(a, n//2, x, y, is_full, 1)

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt_white = 0
cnt_blue = 0


func(arr, n, n, n, False, 0)
func(arr, n, n, n, False, 1)
print(cnt_white, cnt_blue, sep='\n')