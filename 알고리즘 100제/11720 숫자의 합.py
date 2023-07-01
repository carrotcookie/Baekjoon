import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(input().rstrip())
answer = 0

for num in num_lst:
    answer += int(num)

print(answer)