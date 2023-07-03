import sys

input = sys.stdin.readline

n = numerator = int(input())
denominator = int(input())
output = numerator / denominator
tmp = []
idx = 0
rest = []

for i in range(10000):
    quotient = numerator // denominator
    tmp.append(quotient)
    
    if quotient == 0:
        rest.append(numerator)
        numerator *= 10
        continue
    else:
        numerator %= denominator
        if numerator in rest:
            idx = rest.index(numerator)
            break
        rest.append(numerator)
        numerator *= 10
    
    if numerator == 0:
        m = n / denominator
        result = []
        if m % 1:
            result.append(str(tmp[0]))
            result.append(str('.'))
            
        for i in range(1, len(rest)):
            result.append(str(tmp[i]))

        print(''.join(i for i in result))
        exit()

result = []
result.append(str(tmp[0]))
result.append(str('.'))
for i in range(1, idx + 1):
    result.append(str(tmp[i]))
result.append(str('('))
for i in range(-len(rest) + idx, 0, 1):
    result.append(str(tmp[i]))
result.append(str(')'))

print(''.join(i for i in result))