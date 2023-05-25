import sys
input = sys.stdin.readline

for _ in range(int(input())):
    str_input = list(input().rstrip())
    left, right = [], []

    for ch in str_input:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)
    
    right = list(reversed(right))

    print(*(left + right), sep = '')