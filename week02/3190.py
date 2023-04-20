from collections import deque
import sys

n = int(input())
MAP = [[0] * n for _ in range(n)]
rotate_info = deque()
snake_pos = deque([(0, 0)])
dir_lst = [(0, 1), (-1, 0), (0, -1), (1, 0)]
my_dir_idx = 0
count = 0

for _ in range(int(input())):
    apple_x, apple_y = map(int, sys.stdin.readline().split())
    MAP[apple_x - 1][apple_y - 1] = 1

for _ in range(int(input())):
    dir_delay, dir_rotate = sys.stdin.readline().split()
    rotate_info.append([int(dir_delay), dir_rotate])

while True:
    # 현재 머리 좌표가 이동방향에 맞게 좌표가 더해짐
    x, y = snake_pos[0][0] + dir_lst[my_dir_idx][0], snake_pos[0][1] + dir_lst[my_dir_idx][1]
    count += 1

    # 머리가 나아갈 칸이 맵 범위 밖이면 종료
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        print(count)
        sys.exit()
    
    # 꼬리는 따라오지 않는 상태에서 머리 먼저 늘어남
    snake_pos.appendleft((x, y))

    # 머리가 나아간 칸에 꼬리가 존재한다면 종료
    for i in range(1, len(snake_pos)):
        if snake_pos[0] == snake_pos[i]:
            print(count)
            sys.exit()

    if MAP[x][y] == 1:
        # 움직인 곳에 사과가 있을 때
        # 맨 끝 꼬리는 변함 없음
        MAP[x][y] = 0
    else:
        # 사과가 없다면 맨 끝 꼬리는 앞으로 나아가서 없어짐
        snake_pos.pop()

    # 입력해준 방향전환 정보가 남아있다면
    if rotate_info:
        # 입력한 시간이 되었을 때 방향 전환 해주기
        if count == rotate_info[0][0]:
            # 방향 읽기
            dir = rotate_info.popleft()[1]
            
            if dir == 'L':
                # 왼쪽이면 현재 인덱스 +1
                my_dir_idx += 1

                # 범위에 맞게 줄여줌
                if my_dir_idx > 3:
                    my_dir_idx -= 4

            elif dir == 'D':
                # 오른쪽이면 현재 인덱스 -1
                my_dir_idx -= 1

                # 범위에 맞게 줄여줌
                if my_dir_idx < 0:
                    my_dir_idx += 4

            # 인덱스 +1 -1 해주면 방향이 맞게 dir_lst = [(0, 1), (-1, 0), (0, -1), (1, 0)]를 잘 설정해줬음