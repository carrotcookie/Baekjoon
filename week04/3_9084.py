import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    goal_money = int(input())
    dp = [0] * (goal_money + 1)
    dp[0] = 1

    # dp[i] 를 i원을 낼 수 있는 경우의 수라고 한다면
    # 현재 단위가 coin일 때 dp[i - coin]이 있다면 dp[i]는 당연히 존재
    # 주어진 동전들별로 누적시켜야 하니
    # dp[i] += dp[i - coin]
    for coin in coins:
        for i in range(coin, goal_money + 1):
                dp[i] += dp[i - coin]
                # print(*dp)

    print(dp[goal_money])