import sys
input = sys.stdin.readline

n, k = map(int, input().split())
order = list(map(int, input().split()))
using = []
ans = 0

for i in range(k):
    # 현재 사용해야할 물건이 이미 사용중이면 continue
    if order[i] in using: continue
    # 사용중인 물건은 아니지만 꽂을 자리가 있다면 꽂고 continue
    if len(using) < n:
        using.append(order[i])
        continue
    # 사용중인걸 빼고 꽂아야 한다면
    index = -1
    dist = -1
    for num in using:
        # 사용중인 물건 중 다시 사용안하는 물건이 있으면 빼고 꽂음
        if num not in order[i:]:
            index = using.index(num)
            break
        # 다시 사용안하는 물건이 없다면 재사용 시기가 늦늘걸 빼고 꽂음
        if order[i:].index(num) > dist:
            dist = order[i:].index(num)
            index = using.index(num)

    # 저장해놓은 물건을 빼고 현재 물건을 꽂는다
    del using[index]
    using.append(order[i])
    ans += 1

print(ans)