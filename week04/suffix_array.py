# import sys
# input = sys.stdin.readline

# s = input().rstrip()
# n = len(s)
# sa = [i for i in range(n)]
# g = [0] * (n + 1)
# ng = [0] * (n + 1)
# t = 1
# cnt = 0

# print()

# for i in range(n):
#     # 첫 문자로 그룹 정해줌
#     # 문자가 같다면 같은번호로 묶일거임
#     g[i] = ord(s[i])

# while t < n:
#     g[n] = -1
#     sa.sort(key = lambda x:(g[x], g[min(x + t, n)]))

#     for i in range(1, n):
#         p, q = sa[i - 1], sa[i]
#         # 처음부터 다른그룹이거나 같아도 다음 글자까지 봤을 때 다른 그룹이라면
#         # 나중꺼가 이전꺼 보다 늦은 순위를 갖게 됨
#         if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
#             ng[q] = ng[p] + 1
#         # 같은 그룹에 다음글자까지 봤을 때에도 같은 그룹일 때
#         else:
#             ng[q] = ng[p]
    
#     if ng[n - 1] == n - 1:
#         break
#     print(ng[:n])

#     g = ng[:]
#     t *= 2
#     cnt += 1

#     for i in sa:
#         print(f'그룹 {g[i] + 1:>3} -> {s[i:]}')
#     print(f'---------------------{t}번째 글자까지')
#     print()

# print('Suffix Array---------------------')
# for i in sa:
#         print(f'{s[i:]}')

#################################################################################################

import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
sa = [i for i in range(n)]
g = [0] * (n + 1)
ng = [0] * (n + 1)
t = 1
cnt = 0

print()

for i in range(n):
    # 첫 문자로 그룹 정해줌
    # 문자가 같다면 같은번호로 묶일거임
    g[i] = ord(s[i])

pivot = min(g[:n])
tmpArr = sorted(g[:n])
matching_group_num = {}
tmp = 1
for i in range(n):
    if tmpArr[i] > pivot:
        pivot = tmpArr[i]
        tmp += 1
    matching_group_num[pivot] = tmp

sa.sort(key = lambda x:g[x])
for i in range(n):
    print(f'그룹 {matching_group_num[g[sa[i]]]:>2}  ->  {s[sa[i]:]}')
print(f'---------------------{t}번째 글자까지')
print()

while t < n:
    g[n] = -1
    sa.sort(key = lambda x:(g[x], g[min(x + t, n)]))

    for i in range(1, n):
        p, q = sa[i - 1], sa[i]
        # 처음부터 다른그룹이거나 같아도 다음 글자까지 봤을 때 다른 그룹이라면
        # 나중꺼가 이전꺼 보다 늦은 순위를 갖게 됨
        if g[p] != g[q] or g[min(p + t, n)] != g[min(q + t, n)]:
            ng[i] = ng[i - 1] + 1
        # 같은 그룹에 다음글자까지 봤을 때에도 같은 그룹일 때
        else:
            ng[i] = ng[i - 1]

    for i in range(n):
        print(f'그룹 {ng[i] + 1:>2}  ->  {s[sa[i]:]}')
    print(f'---------------------{t * 2}번째 글자까지')
    print()

    # 그룹이 길이 만큼 나뉘었으면 종료
    if ng[n - 1] == n - 1:
        break
    
    for i in range(n): g[sa[i]] = ng[i]

    t *= 2
    cnt += 1

# print('Suffix Array---------------------')
# for i in sa:
#         print(f'{s[i:]}')

print('Suffix Array---------------------')
for i in sa:
        print(f'{i}')