import sys
import heapq

coordis = []            # 좌표들 저장
valid_coordis = []      # 실제 철로 길이와 비교할 좌표들 
heap = []
d = 0                   # 철로 길이
result = 0              # 최대 수

# 좌표 입력
for _ in range(int(input())):
    tmp = list(map(int, sys.stdin.readline().split()))
    coordis.append(sorted(tmp))

print(coordis)
# 철로 길이 입력
d = int(input())

# 두 점 사이의 길이가 d 이하인 좌표만 넣어줌
for coordi in coordis:
    if abs(coordi[0] - coordi[1]) > d: continue
    valid_coordis.append(coordi)

print(valid_coordis)

# 끝점 기준으로 오름차순
valid_coordis = sorted(valid_coordis, key = lambda x: x[1])
print(valid_coordis)

for coordi in valid_coordis:

    # 없으면 넣어줌
    if not heap:
        heapq.heappush(heap, coordi)
        continue

    # 안에 있던 시작점이 현재 끝점에서 d만큼 뺀것보다 작다면 범위 안에 없으니 제거
    # 시작점이 작은거부터 제거해야 원하는대로 동작 -> 항상 최소힙 상태면 가능
    while heap[0][0] < coordi[1] - d:
        # 시작점 작은거 날림
        heapq.heappop(heap)
        # 날리고 비어있으면 종료
        if not heap:
            break

    # 제거할게 없으면 현재 좌표 넣어줌    
    heapq.heappush(heap, coordi)
    # 최대 수 갱신
    result = max(result, len(heap))

print(result)