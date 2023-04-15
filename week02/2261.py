import sys

def func(depth, x1, x2, y1, y2, width, height):
    if width < 1 and height < 1:
        return

    if width // 2:
        width //= 2
    if height // 2:
        height //= 2


    record = []
    count = 0

    for i in range(n):
        if x1 <= x_lst[i] <= x2 and y1 <= y_lst[i] <= y2:
            count += 1
            record.append((x_lst[i], y_lst[i]))
            if count == 2:
                dist = min(dist, (record[0][0] - record[1][0]) ** 2 + (record[0][1] - record[1][1]) ** 2)
                break
    record.clear()

    func(depth + 1, border_x - width, border_x, border_y, border_y + height, width, height)
    func(depth + 1, border_x, border_x + width, border_y, border_y + height, width, height)
    func(depth + 1, border_x - width, border_x, border_y - height, border_y, width, height)
    func(depth + 1, border_x, border_x + width, border_y - height, border_y, width, height)

n = int(input())
x_lst = []
y_lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_lst.append(x)
    y_lst.append(y)

x_lst_sort = sorted(x_lst)
y_lst_sort = sorted(y_lst)

width = x_lst_sort[-1] - x_lst_sort[0] # 6
height = y_lst_sort[-1] - y_lst_sort[0] # 6
border_x = (x_lst_sort[-1] + x_lst_sort[0]) // 2 # x = 1
border_y = (y_lst_sort[-1] + y_lst_sort[0]) // 2 # y = 0

dist = sys.maxsize

func(0, border_x, border_y, width, height)