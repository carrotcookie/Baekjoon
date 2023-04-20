import sys

# 바텀업 방식으로 보면 이미 2개의 좌표 거리 부터 해서 최소 거리를 가지고 올라옴
# 나중에 실행되는 함수에서는 이 거리와 비교하여 맡고있는 영역에서 2개씩 뽑아 바로 거리 계산을 하는게 아닌
# x 좌표 거리만 봤을 때 최소 dist보다 멀면 거르고, dist보다 가까우면 일단 후보군에 올림
# 후보군에 올라온 좌표 리스트를 y축 정렬해서 y축 거리로만 비교 했을 때 dist보다 가까우면 그제서야 제대로된 거리 계산을 해주고 min()

# 요약: 눈대중으로 봐도 먼 좌표사이의 거리는 후보군 탈락
#       후보군에 올라온 것들을 y좌표 기준으로 눈대중 검사하고 통과한 좌표들에 한해서만 실제 거리 계산

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def func(a, left, right):

    if left == right:
        return sys.maxsize
    if right - left == 1:
        return dist(a[left], a[right])
    
    mid = (left + right) // 2
    min_dist = min(func(a, left, mid - 1), func(a, mid + 1, right))

    target_pos_li = []
    for i in range(left, right + 1):
        if (a[mid][0] - a[i][0]) ** 2 < min_dist:
            target_pos_li.append(a[i])

    target_pos_li = sorted(target_pos_li, key = lambda x: x[1])
    
    t = len(target_pos_li)
    for i in range(t - 1):
        for j in range(i + 1, t):
            if (target_pos_li[i][1] - target_pos_li[j][1]) ** 2 < min_dist:
                min_dist = min(min_dist, dist(target_pos_li[i], target_pos_li[j]))
            else:
                break

    return min_dist


n = int(input())
pos_li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pos_li = sorted(pos_li)

print(func(pos_li, 0, n - 1))