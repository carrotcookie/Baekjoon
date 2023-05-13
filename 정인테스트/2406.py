import sys
input = sys.stdin.readline

def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y

n, m = map(int, input().split())
p = [i for i in range(n + 1)]
edge = []

# 출력정보
min_cost = 0
count = 0
info = []

# 입력된 노드끼리 결합
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a, b)

# 1번 컴퓨터에 대한 입력 필요없음
dummy_input = input() 
# 입력되는 정보에서 필요한것은 대각절반
for i in range(2, n + 1):
    costs = list(map(int, input().split()))

    for j in range(i, n):
        edge.append((costs[j], i, j + 1))

# 비용 오름차순 정렬
edge.sort()

# 안 묶여있으면 묶고 출력정보 갱신
for cost, i, j in edge:
    if find_parent(i) != find_parent(j):
        union_parent(i, j)
        min_cost += cost
        count += 1
        info.append((i, j))

print(min_cost, count)
for i in range(count):
    a, b = info[i]
    print(a, b)