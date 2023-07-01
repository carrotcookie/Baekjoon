import sys
input = sys.stdin.readline

len1, len2 = map(int, input().split())
num_lst_1 = list(map(int, input().split()))
num_lst_2 = list(map(int, input().split()))

print(*sorted(num_lst_1 + num_lst_2))