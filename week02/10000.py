import sys

# 1. 틀림
# n = int(input())
# stack = []
# count = 1

# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     left = x - y
#     right = x + y

#     count += 1
#     stack.append((left, right))

# bonus = 0
# i, j = stack.pop()
# while stack:
#     next_i, next_j = stack.pop()

#     if i == next_i or i == next_j or j == next_i or j == next_j:
#         bonus += 1

# print(count + bonus // 2)

######################################################################################################################

# 2.
n = int(input())
a = []
stack = []
count = 0

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    a.append([x - r, '(']) # 아스키코드 40
    a.append([x + r, ')']) # 아스키코드 41

# x좌표를 우선적으로 오름차순 후
# x좌표가 같다면 )를 먼저 오게 하기 위해 내림차순 한다
a.sort(key = lambda x : (x[0], -ord(x[1])))
stack.append({'x_pos': a[0][0], 'state': 'normal'})

for i in range(1, n * 2):

    # ( 가 들어올 때
    # 이전의 좌표와 같다면 내접하는것이니 상태변경
    if a[i][1] == '(':
        if stack and stack[-1]['x_pos'] == a[i][0]:
            stack[-1]['state'] = 'internal'
        stack.append({'x_pos': a[i][0], 'state': 'normal'})
    
    # ) 가 들어올 때
    # 이전의 상태가 내접 상태였으면 +2 아니라면 +1
    else:
        if stack[-1]['state'] == 'internal':
            count += 2
        else:
            count += 1

        stack.pop()

        # 닫히고 나서 이어지는지 판단하기 위해 현재좌표와 다음좌표가 다르다면
        # 끊어진 것이니 이전꺼 상태 변경
        if i + 1 <= 2 * n - 1 and a[i + 1][0] != a[i][0]:
            stack[-1]['state'] = 0

print(count + 1)