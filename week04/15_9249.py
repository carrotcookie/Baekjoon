import sys
input = sys.stdin.readline

T = '0' + input().rstrip()
S = '0' + input().rstrip()

lenT = len(T)
lenS = len(S)

result = []
max_length = 0

if lenT >= lenS:
    for i in range(1, lenS):
        tmp = S[i:]
        if tmp in T:
            length = len(tmp)
            if length > max_length:
                max_length = length
                result.append((length, i))

print(result[-1][0])
print(S[result[-1][1]:])