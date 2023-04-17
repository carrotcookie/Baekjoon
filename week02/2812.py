n, k = map(int, input().split())
input = input()
stack = []
cnt1 = 0

for num in input:
    while stack and stack[-1] < num and k:
        stack.pop()
        k -= 1

    stack.append(num)

if k:
    # 남아있는 k만큼 뒤에서부터 지움
    print(*stack[:len(stack)-k], sep = '')
else:
    print(*stack, sep = '')