import sys
input = sys.stdin.readline

bracket = list(input().strip())
stack = []
ans = 0

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(bracket[i])
    else:
        # 레이저라면 잘리니까 현재 들어간 막대기만큼 더해줌
        if bracket[i - 1] == '(':
            stack.pop()
            ans += len(stack)
        # 막대기 원본 개수
        else:
            stack.pop()
            ans += 1

print(ans)