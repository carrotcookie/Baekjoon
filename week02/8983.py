# 1. 시간초과
# import sys

# m, n, l = map(int, input().split())
# sniper = list(map(int, sys.stdin.readline().split()))
# animal = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# shot = []

# for i in range(m):
#     for lst in animal:
#         if lst not in shot and abs(sniper[i] - lst[0]) + lst[1] <= l:
#             shot.append(lst)

# print(len(shot))

#############################################################################################

# 2.
import sys

def find_index(a, x):
    # 정렬된 배열에서 x가 들어갈 인덱스 결정
    left = 0
    right = len(a) - 1
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if a[mid] >= x:
            right = mid - 1
            result = mid
        else:
            left = mid + 1
            result = mid + 1

    return result

m, n, l = map(int, input().split())
sniper = list(map(int, sys.stdin.readline().split()))
animal = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = 0

sniper.sort()

# 동물 좌표마다 잡을 수 있는지 검사
for x, y in animal:

    # y좌표가 사거리보다 크면 못잡음. 다음 좌표 검사
    if y > l: continue

    # 이거 쓰고 idx + 1 검사는 뺄라 했는데 더 느림
    # if sniper.count(x):
    #     count += 1
    #     continue

    # 현재 x 좌표와 가까운 사냥꾼 좌표 인덱스를 구하기 위해
    idx = find_index(sniper, x)

    # 동물의 x 좌표와 가장 가까운 사냥꾼 좌표를 모르니 총 3개 검사
    for i in [idx + 1, idx, idx - 1]:
        # 인덱스 범위를 넘지않고 사거리 내에 있다면 카운팅 후 빠져나옴
        if 0 <= i < m and abs(sniper[i] - x) + y <= l:
            count += 1
            break
    
print(count)

#############################################################################################

# 3.
# import sys

# def check(x, y):
#     # y축이 사거리보다 높으면 False
#     if y > l:
#         return 0
    
#     left = 0
#     right = m - 1

#     while left <= right:

#         mid = (left + right) // 2

#         if 0 <= mid < m and abs(x - sniper[mid]) + y <= l:
#             return 1
#         if sniper[mid] < x:
#             left = mid + 1
#         elif sniper[mid] > x:
#             right = mid - 1
   
#     return 0

# input = sys.stdin.readline
# m, n, l = map(int,input().split())

# sniper = list(map(int,input().split()))
# sniper.sort()

# count = 0

# for i in range(n):
#     animal_pos = list(map(int,input().split()))

#     if check(animal_pos[0], animal_pos[1]):
#         count += 1

# print(count)