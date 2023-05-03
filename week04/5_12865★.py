import sys
input = sys.stdin.readline

# dp[i][j]를 i번째 물건까지 봤을 때 무게가 j인 가방에서 가질 수 있는 최대가치라 하자

n, k = map(int, input().split())
items = []
dp = [[0] * (k + 1) for _ in range(n)]

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

for i in range(n):
    for j in range(1, k + 1):
        w, v = items[i]
        # 현재 가방의 무게가 현재 아이템 무게를 소화하지못하면
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 현재 아이템을 넣을 수 있다면
        # 현재 아이템 무게를 뺀 무게의 가방에서 가질 수 있는 최대가치에 현재 아이템 가치를 더하거나
        # 현재 아이템을 넣지않거나
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])
            
print(dp[-1][-1])

print()
for i in range(n):
    for j in range(1, k + 1):
        print(f'{dp[i][j]:>3}', end = '')
    print()