import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    goal_money = int(input())
    dp = [0] * (goal_money + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, goal_money + 1):
                dp[i] += dp[i - coin]
                print(*dp)

    print(dp[goal_money])