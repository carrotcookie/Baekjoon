import sys
import heapq
from collections import deque

# 1920. 수 찾기
# def do_exist(a, x):
#     n = len(a)
#     left, right = 0, n - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if a[mid] > x:
#             right = mid - 1
#         elif a[mid] < x:
#             left = mid + 1
#         else:
#             return 1
        
#     return 0

# n = int(input())
# a = list(map(int, sys.stdin.readline().split()))
# m = int(input())
# b = list(map(int, sys.stdin.readline().split()))

# a = sorted(a)
# for num in b:
#     print(do_exist(a, num))

#######################################################################################################################

# 2805. 나무 자르기
# def max_cut_height(a, m):
#     left, right = 0, max(a)
#     result = 0      #가장 많이 가져갈 수 있는 나무 높이

#     while left <= right:
#         tmp = 0     # 가져갈 수 있는 나무 높이
#         mid = (left + right) // 2

#         for h in a:
#             if h > mid:
#                 tmp += h - mid
        
#         if tmp >= m:
#             # 필요한것 이상으로 가져갈 수 있으면
#             # 더 높이 잘라도 괜찮지 않을까하면서 mid를 높여준다 -> 우측 영역 탐색
#             left = mid + 1
#             result = max(result, mid)   # 필요한만큼 가져갈 수 있을 때 자른 높이 높은걸로 갱신
#         else:
#             # 필요한 만큼 못 가져가면 덜 잘라서 더 많이 얻자 -> 좌측 영역 탐색
#             right = mid -1

#     return result

# n, m = map(int, input().split())
# a = list(map(int, sys.stdin.readline().split()))

# print(max_cut_height(a, m))

#######################################################################################################################

# 2110. 공유기 설치
# def max_neighbor_dist(a, c):
#     left, right = 1, a[-1] - a[0]
#     n = len(a)
#     result = 0

#     while left <= right:
#         # 맨 첫 위치는 무조건 설치
#         recent_install_pos = 0
#         count = 1

#         mid = (left + right) // 2

#         for i in range(1, n):
#             # 최근 설치한 위치에서부터 현재 위치에 mid 간격만큼 설치 가능하면
#             # 최근 설치 위치 갱신 및 카운팅
#             if a[i] - a[recent_install_pos] >= mid:
#                 recent_install_pos = i
#                 count += 1
#                 # c만큼 설치 했으면 탈출
#                 if count == c:
#                     break
        
#         # c만큼 설치 가능했으면 더 넓은 간격으로도 설치할 수 있나 확인 -> 우측 영역 확인
#         if count == c:
#             left = mid + 1
#             result = max(result, mid)
#         # c만큼 설치 못했으면 더 좁은 간격으로 설치할 수 있나 확인 -> 좌측 영역 확인
#         else:
#             right = mid - 1

#     return result

# n, c = map(int, input().split())
# a = [int(sys.stdin.readline()) for _ in range(n)]
# a = sorted(a)

# print(max_neighbor_dist(a, c))

#######################################################################################################################

# 2470. 두 용액
# def find_pair(a):
#     # 정렬 되어있으니 양 끝을 투포인터로 설정
#     pl, pr = 0, len(a) - 1
#     value = sys.maxsize
#     result = []

#     while pl < pr:
#         # 두 용액의 특성값
#         tmp = a[pl] + a[pr]

#         # 0은 바로 리턴
#         if tmp == 0:
#             result = [a[pl], a[pr]]
#             return result
#         # 현재 value에 저장되어있는 특성값보다 작으면
#         # value 갱신하고 현재 두개의 포인터 가르키는 값 저장
#         elif tmp > 0:
#             if tmp < value:
#                 value = tmp
#                 result = [a[pl], a[pr]]
#             pr -= 1     # 합이 0보다 크다면 우측 포인터를 좌측으로 옮겨서 양의 값을 줄임
#         elif tmp < 0:
#             if -tmp < value:
#                 value = -tmp
#                 result = [a[pl], a[pr]]
#             pl += 1     # 합이 0보다 작다면 좌측 포인터를 우측으로 옮겨서 음의 값을 줄임
    
#     return result

# n = int(input())
# a = list(map(int, sys.stdin.readline().split()))
# a = sorted(a)

# if n == 2:
#     print(a[0], a[1])
#     sys.exit()

# print(*find_pair(a), sep = ' ')

#######################################################################################################################

# 11053. 가장 긴 증가하는 부분 수열
# n = int(input())
# a = list(map(int, input().split()))
# dp = [1] * n

# for i in range(n):
#     for j in range(i):
#         if a[i] > a[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))

#######################################################################################################################

# 8983. 사냥꾼
# def find_correct_index(a, x):
#     left, right = 0, len(a) - 1
#     result = 0

#     while left <= right:
#         mid = (left + right) // 2

#         if a[mid] == x:
#             return mid
#         elif a[mid] > x:
#             right = mid - 1
#             result = mid
#         else:
#             left = mid + 1
#             result = mid + 1

#     return result            

# m, n, l = map(int, input().split())
# sniper_pos = list(map(int, sys.stdin.readline().split()))
# sniper_pos = sorted(sniper_pos)
# count = 0

# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     if y > l: continue

#     # 동물의 x좌표가 들어오면 가까운 사대의 인덱스 찾기
#     idx = find_correct_index(sniper_pos, x)

#     # 가장 가까운 인덱스를 찾은게 아니여서
#     # idx 와 idx - 1 -> 2개의 사대와 비교 해야함
#     try:
#         if abs(sniper_pos[idx] - x) + y <= l:
#             count += 1
#             continue
#     except:
#         pass

#     try:
#         if abs(sniper_pos[idx - 1] - x) + y <= l:
#             count += 1
#             continue
#     except:
#         pass

# print(count)

#######################################################################################################################

# 2630. 색종이 만들기
# def count_paper(row, col, size):
#     # 현재 구역이 전부 같은 색상이면 카운팅
#     # 아니면 구역을 4등분해서 구역별로 또 검사
#     global white, blue

#     # 현재 size * size를 전부 같나 검사해줄거라
#     # 스타트 색상 저장
#     color = a[row][col]
#     next_size = size // 2

#     for i in range(row, row + size):
#         for j in range(col, col + size):
#             # 다른 색이 나오는 순간 쪼개고 종료
#             if a[i][j] != color:
#                 count_paper(row, col, next_size)                            # 1사분면
#                 count_paper(row, col + next_size, next_size)                # 2사분면
#                 count_paper(row + next_size, col, next_size)                # 3사분면
#                 count_paper(row + next_size, col + next_size, next_size)    # 4사분면
#                 return
    
#     # 전부 같은 색이었다면 카운팅
#     if color == 0:
#         white += 1
#     else:
#         blue += 1

# n = int(input())
# a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# white, blue = 0, 0

# count_paper(0, 0, n)
# print(white, blue, sep = '\n')

#######################################################################################################################

# 1629. 곱셈
# def find_rest(a, b, c):
#     # 나머지 분배법칙
#     if b == 1:
#         return a % c
    
#     tmp = find_rest(a, b // 2, c)

#     if b % 2 == 0:
#         return tmp * tmp % c
#     else:
#         return tmp * tmp * a % c

# a, b, c = map(int, input().split())
# print(find_rest(a, b, c))

#######################################################################################################################

# 6549. 히스토그램에서 가장 큰 직사각형 ★★★

# while True:
#     hs = []
#     input = list(map(int, sys.stdin.readline().split()))
#     n, h_lst = input[0], input[1:]
#     stack = []
#     result = 0
#     if n == 0: sys.exit()

#     for i in range(n):
#         width = 0

#         while stack and stack[-1][1] > h_lst[i]:
#             width += stack[-1][0]
#             result = max(result, width * stack[-1][1])
#             hs.append(width * stack[-1][1])
#             stack.pop()
        
#         width += 1
#         stack.append([width, h_lst[i]])

#     width = 0
#     while stack:
#         width += stack[-1][0]
#         result = max(result, width * stack[-1][1])
#         hs.append(width * stack[-1][1])
#         stack.pop()

#     print(result)
#     print(hs)

#######################################################################################################################

# 10830. 행렬 제곱 ★★★
# def mul_mod(a, b):
#     c = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             tmp = 0
#             for k in range(n):
#                 tmp += a[i][k] * b[k][j]
#             c[i][j] = tmp % 1000
    
#     return c

# def func(a, b):
#     if b == 1:
#         for i in range(n):
#             for j in range(n):
#                 a[i][j] %= 1000
#         return a
    
#     tmp = func(a, b // 2)

#     if b % 2 == 0:
#         return mul_mod(tmp, tmp)
#     else:
#         return mul_mod(mul_mod(tmp, tmp), a)
    
# n, b = map(int, input().split())
# a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
# for row in func(a, b):
#     print(*row)

#######################################################################################################################

# 10828. 제로
# stack = deque()

# for _ in range(int(input())):
#     n = int(sys.stdin.readline())
#     if n:
#         stack.append(n)
#     else:
#         stack.pop()

# print(sum(stack))

#######################################################################################################################

# 9012. 괄호
# for i in range(int(input())):
#     bracket = sys.stdin.readline().rstrip()
#     stack = []

#     for ch in bracket:
#         if not stack:
#             if ch == ')':
#                 stack.append(ch)
#                 break
#             stack.append(ch)
#             continue
#         if ch == ')':
#             stack.pop()
#         else:
#             stack.append(0)

#     print('NO' if stack else 'YES')

#######################################################################################################################

# 17608. 막대기
# stack = []

# for i in range(int(input())):
#     h = int(sys.stdin.readline())

#     if not stack:
#         stack.append(h)
#         continue

#     while stack and stack[-1] <= h:
#         stack.pop()
#     stack.append(h)

# print(len(stack))

#######################################################################################################################

# 2493. 탑
# n = int(input())
# a = list(map(int, sys.stdin.readline().split()))
# stack = []
# result = []

# for i in range(n):
#     # 아무것도 없으면 넣고 현재 탑의 수신자 인덱스는 0이다
#     if not stack:
#         stack.append([i, a[i]])
#         result.append(0)
#         continue
#     # 스택이 존재하고 나보다 작으면 계속 빼줌
#     while stack and stack[-1][1] < a[i]:
#         stack.pop()
#     # 작은것들 다 빼고 남아있으면 그거 (인덱스 + 1) 이 현재 탑의 수신자 인덱스이다
#     # 출력 인덱스는 0이 아니라 1부터 시작이여서 1을 더해준거임
#     if stack:
#         result.append(stack[-1][0] + 1)
#     # 없다면 수신자 인덱스는 0이다
#     else:
#         result.append(0)

#     stack.append([i, a[i]])

# print(*result)

#######################################################################################################################

# 10000. 원 영역 ★★★
# n = int(input())
# circle_info = []
# stack = []
# count = 1

# for _ in range(n):
#     r, c = list(map(int, sys.stdin.readline().split()))
#     circle_info.append([r - c, '('])
#     circle_info.append([r + c, ')'])
# circle_info = sorted(circle_info, key = lambda x : (x[0], -ord(x[1])))

# for i in range(2 * n):
#     if stack:
#         # 연속으로 open이 들어오고 좌표도 같다면 스택에 있는 open을 내접상태로 바꿔줌
#         if circle_info[i][1] == '(' and circle_info[i][0] == stack[-1]['pos']:
#             stack[-1]['state'] = 2
#         # close가 들어오면 상태에 따라 점수 추가하고, pop 후 비어있으면 컨티뉴, open상태가 남아있다면
#         # 이어지는지 확인하기 위해 현재 좌표와 다음좌표가 같은지 확인
#         elif circle_info[i][1] == ')':
#             count += stack.pop()['state']
#             if not stack:
#                 continue
#             if i + 1 < 2 * n and circle_info[i + 1][0] != circle_info[i][0]:
#                 stack[-1]['state'] = 1
#             continue

#     stack.append({'pos': circle_info[i][0], 'shape': circle_info[i][1], 'state': 1})

# print(count)

#######################################################################################################################

# 2504. 괄호의 값
# bracket = input()
# stack = []
# tmp = 1
# result = 0

# for i in range(len(bracket)):
#     if bracket[i] == '(':
#         tmp *= 2
#         stack.append(bracket[i])
#     elif bracket[i] == '[':
#         tmp *= 3
#         stack.append(bracket[i])

#     elif bracket[i] == ')':
#         if not stack or stack[-1] == '[':
#             result = 0
#             break
#         # 바로 전이 짝꿍 이었을때만 실제 점수에 반영
#         if bracket[i - 1] == '(':
#             result += tmp

#         stack.pop()
#         tmp //= 2
#     elif bracket[i] == ']':
#         if not stack or stack[-1] == '(':
#             result = 0
#             break
#         # 바로 전이 짝꿍 이었을때만 실제 점수에 반영
#         if bracket[i - 1] == '[':
#             result += tmp
        
#         stack.pop()
#         tmp //= 3

# if stack:
#     print(0)
# else:
#     print(result)

#######################################################################################################################

# 2812. 크게 만들기 ★★★
# 현재 들어가는 숫자보다 작은게 있다면 뺀다
# 뺄때마다 횟수를 카운트하고 k번을 만족하게되면 빼는 과정은 멈추고 남아있는 것들은 전부 넣어줌
# 끝까지 돌았는데 k번 미만으로 빼줬다면 최종 스택에서 남은 횟수만 위에서 부터 빼면 됨
# n, k = map(int, input().split())
# target = input()
# stack = []

# for num in target:
#     tmp = int(num)

#     while stack and stack[-1] < tmp and k:
#         stack.pop()
#         k -= 1
    
#     stack.append(tmp)

# if k:
#     print(*stack[:len(stack) - k], sep = '')
# else:
#     print(*stack, sep = '')

#######################################################################################################################

# 2164. 카드2
# n = int(input())
# a = deque([i for i in range(1, n + 1)])

# while len(a) > 1:
#     a.popleft()
#     a.append(a.popleft())

# print(*a)

#######################################################################################################################

# 11866. 요세푸스 문제 0
# n, k = map(int, input().split())
# a = deque([i for i in range(1, n + 1)])
# result = []

# while a:
#     # k - 1번 만큼 앞에를 빼서 뒤로 넣어주고
#     for _ in range(k - 1):
#         a.append(a.popleft())
#     # k번째에는 앞에를 빼서 결과 배열에 넣어줌
#     result.append(a.popleft())

# print('<', end = '')
# print(*result, sep = ', ', end = '')
# print('>')

#######################################################################################################################

# 3190. 뱀
# 이동할 때 머리를 먼저 이동시켜보고 판단 
# 이동할 칸에 사과가 있다면 새 머리 좌표만 appendleft 하면 됨
# 이동할 칸에 사과가 없다면 새 머리 좌표를 appendleft 하고 맨 뒤만 pop 해주면 됨

# n = int(input())
# MAP = [[0] * n for _ in range(n)]
# rotate_info = deque()
# snake = deque([[0, 0]])
# dir_lst = [[0, 1], [-1, 0], [0, -1], [1, 0]]
# dir_idx = 0
# count = 0

# # 맵 좌표 어딘가 사과 넣어주기
# # 사과 좌표는 1행 1열 기준으로 되어있으니 넣어줄 때 -1을 해야함
# # 사과는 1로 표시
# for _ in range(int(input())):
#     x, y = map(int, sys.stdin.readline().split())
#     MAP[x - 1][y - 1] = 1

# # 방향 변환 정보 넣어주기
# for _ in range(int(input())):
#     time, dir = map(str, sys.stdin.readline().split())
#     rotate_info.append([int(time), dir])

# while True:
#     count += 1
#     # 나아갈 좌표
#     nx, ny = snake[0][0] + dir_lst[dir_idx][0], snake[0][1] + dir_lst[dir_idx][1]

#     # 이동할 좌표가 이미 존재한다면 죽음
#     if [nx, ny] in snake:
#         break
#     # 맵밖으로 나가도 죽음
#     if not 0 <= nx < n or not 0 <= ny < n:
#         break
    
#     snake.appendleft([nx, ny])

#     if MAP[nx][ny] == 1:
#         MAP[nx][ny] = 0
#     else:
#         # 사과 못먹으면 맨 뒤 빼줌
#         snake.pop()

#     # 이동에 성공하면 그림 그려봄
#     for i in range(n + 2):
#         for j in range(n + 2):
#             if [i - 1, j - 1] in snake:
#                 print('○', end = ' ')
#                 continue
#             if i == 0 or i == n + 1 or j == 0 or j == n + 1:
#                 print('■', end = ' ')
#                 continue
#             print(' ', end = ' ')
#         print()
#     print(f'------------------------------------------ {count}')

#     # 방향 변환 정보에 따른 방향 인덱스 변경
#     if rotate_info and count == rotate_info[0][0]:
#         info = rotate_info.popleft()[1]

#         if info == 'L':
#             dir_idx = dir_idx + 1 if dir_idx != 3 else 0 
#         else:
#             dir_idx = dir_idx - 1 if dir_idx != 0 else 3

# print(count)

#######################################################################################################################

# 11279. 최대 힙
# heap = []

# for _ in range(int(input())):
#     x = int(sys.stdin.readline())
#     if x == 0:
#         if not heap:
#             print(0)
#         else:
#             print(-heapq.heappop(heap))
#         continue

#     heapq.heappush(heap, -x)

#######################################################################################################################

# 1655. 가운데를 말해요
# n = int(input())
# left_heap = []
# right_heap = []

# for i in range(n):
#     num = int(sys.stdin.readline())

#     if len(left_heap) == len(right_heap):
#         heapq.heappush(left_heap, -num)
#     else:
#         heapq.heappush(right_heap, num)

#     if right_heap and -left_heap[0] > right_heap[0]:
#         left = heapq.heappop(left_heap)
#         right = heapq.heappop(right_heap)
#         heapq.heappush(left_heap, -right)
#         heapq.heappush(right_heap, -left)

#     print(-left_heap[0])

#######################################################################################################################

# 1715. 카드 정렬하기
# n = int(input())
# heap = []
# result = 0

# for _ in range(n):
#     heapq.heappush(heap, int(sys.stdin.readline()))

# while len(heap) > 1:
#     num1 = heapq.heappop(heap)
#     num2 = heapq.heappop(heap)
#     sum = num1 + num2
#     result += sum
#     heapq.heappush(heap, sum)

# print(result)

#######################################################################################################################

# 13334. 철로
# n = int(input())
# tmp_start_end_pos = []
# start_end_pos = []
# heap = []
# result = 0

# # 시작점 끝점을 정렬해서 넣어줌
# for _ in range(n):
#     h, o = map(int, sys.stdin.readline().split())
#     tmp_start_end_pos.append(sorted([h, o]))

# d = int(input())

# # 시작점 끝점 거리가 d 이하인 것들을 새 배열에 넣어줌
# for i in range(n):
#     if abs(tmp_start_end_pos[i][0] - tmp_start_end_pos[i][1]) > d: continue
#     start_end_pos.append(tmp_start_end_pos[i])

# # 시작점 기준으로 내림차순
# start_end_pos = sorted(start_end_pos, key = lambda x: -x[0])

# for start, end in start_end_pos:
#     # 범위 밖에 있으면 빼주고
#     while heap and start + d < -heap[0]:
#         heapq.heappop(heap)

#     # 끝점 정보만 최대힙으로 넣어줌
#     # 시작점부터 철로를 두니 끝점이 멀리있는것부터 비교해줘야 함
#     heapq.heappush(heap, -end)
#     result = max(result, len(heap))

# print(result)

#######################################################################################################################

n = int(sys.stdin.readline())
sorted_location = []
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    sorted_location.append((x, y))
sorted_location.sort()

def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solution(l, r):
    if l == r:
        return float('inf')
    else:
        m = (l + r) // 2
        min_dist = min(solution(l, m), solution(m + 1, r))
        target_list = []
        
        for i in range(m, l - 1, -1):
            if (sorted_location[i][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[i])
            else:
                break

        for j in range(m + 1, r + 1):
            if (sorted_location[j][0] - sorted_location[m][0]) ** 2 < min_dist:
                target_list.append(sorted_location[j])
            else:
                break
                
        target_list.sort(key=lambda x: x[1])
        for i in range(len(target_list) - 1):
            for j in range(i + 1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) ** 2 < min_dist:
                    dist = get_dist(target_list[i], target_list[j])
                    min_dist = min(min_dist, dist)
                else:
                    break
        return(min_dist)

if len(sorted_location) != len(set(sorted_location)):
    print(0)
else:
    print((solution(0, len(sorted_location) - 1)))