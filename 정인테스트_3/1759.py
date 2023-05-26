import sys
input = sys.stdin.readline

def combination(start, depth, dest):
    global tmp

    if depth == dest:
        cnt = 0

        for ch in ['a', 'e', 'i', 'o', 'u']:
            if ch in tmp:
                cnt += 1

        if cnt >= 1 and l - cnt >= 2:
            print(*tmp, sep = '')
            
        return
    
    for i in range(start, c):
        tmp.append(alphabets[i])
        combination(i + 1, depth + 1, dest)
        tmp.pop()

l, c = map(int, input().split())
alphabets = sorted(list(input().split()))
tmp = []
print()

print(alphabets)
combination(0, 0, l)