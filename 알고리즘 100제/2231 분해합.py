import sys
input = sys.stdin.readline

n_str = input().rstrip()
minimum = int(n_str) - len(n_str) * 9
minimum = 0 if minimum < 0 else minimum

for i in range(minimum, int(n_str)):
    i_lst = list(map(int, str(i)))
    constructor = i + sum(i_lst)

    if constructor == int(n_str):
        print(i)
        break
else:
    print(0)