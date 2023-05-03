import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stone = []
max_speed = 0
tmp = 1

# n개짜리 돌에서 최대 낼 수 있는 속도는 max_speed이다
for i in range(1, n + 1):
    tmp += i
    if tmp > n:
        max_speed = i - 1
        break

# for문 검사에서 인덱스 에러때문에 max_speed + 1 인덱스까지 만들어줌
dp = [[sys.maxsize] * (max_speed + 2) for _ in range(n + 1)]
# 1번 돌은 밟은상태에서 시작함
dp[1][0] = 0

for _ in range(m):
    stone.append(int(input()))

for i in range(2, n + 1):
    # 밟을 수 없는 돌이면 continue
    if i in stone: continue
    # i번째 돌을 j속도로 밟는 방법 3가지
    # i-j 번째 돌을 j-1의 속도로 밟고 가속
    # i-j 번째 돌을   j의 속도로 밟고 등속
    # i-j 번째 돌을 j+1의 속도로 밟고 감속
    for j in range(1, max_speed + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

ans = min(dp[n])
print(ans if ans != sys.maxsize else -1)