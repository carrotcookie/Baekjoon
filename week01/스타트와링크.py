n = int(input())
a = []
numbers = []
tmp = []
power_diff = []

for _ in range(n):
    a.append(list(map(int, input().split())))

def cal_power(team):
    another_team = list(set(range(n)) - set(team))

    sum = 0
    for idx, i in enumerate(team):
        for j in team[idx+1:]:
            sum += a[i][j] + a[j][i]

    another_sum = 0
    for idx, i in enumerate(another_team):
        for j in another_team[idx+1:]:
            another_sum += a[i][j] + a[j][i]

    power_diff.append(abs(sum - another_sum))

# nC2 만드는 과정
def recur(start, count):
    if count == n // 2:
        cal_power(tmp)
        return
    
    for i in range(start, n):
        tmp.append(i)
        recur(i + 1, count + 1)
        tmp.pop()

recur(0, 0)
print(min(power_diff))