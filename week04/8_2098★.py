import sys
import math
input = sys.stdin.readline

def func(node, visit):
    min_value = sys.maxsize

    if visit == 0:
        # 기준을 1에서 출발하여 1로 도착하는 걸로 정했음
        return W[node][1] if W[node][1] else sys.maxsize

    for i in pivot:
        # 갈 수 있는 도시가 있으면
        if visit & i:
            # 해당 도시를 사용 가능한 인덱스 번호로 바꿔주고
            idx = int(math.log2(i)) + 1
            # node에서 해당 도시까지 경로가 없으면 continue
            if not W[node][idx]:
                continue
            # 경로가 있으면 해당 도시를 제외한 나머지 도시들 방문해야함
            rest_visit = visit ^ i
            # 아직 계산한것이 아니라면 계산해주고
            if not dp[idx][rest_visit]:
                dp[idx][rest_visit] = func(idx, rest_visit)
            # 이미 계산한것이라면 바로 넣어줌
            min_value = min(min_value, W[node][idx] + dp[idx][rest_visit])

    return min_value

n = int(input())
W = [[0] * (n + 1)]

# dp[i][14] = dp[i][1110] -> i에서 2,3,4를 거쳐서 1로 가는 최소비용
dp = [[None] * (2**n) for _ in range(n + 1)]
# 1, 2, 4, 8 .... 이 들어가는 배열
# 해당 노드를 갈 수 있는지 검사할 때 사용
pivot = [2**i for i in range(n)]

for _ in range(n):
    W.append([0] + list(map(int, input().split())))

print(func(1, 2**n - 1 - 1))