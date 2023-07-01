import sys
input = sys.stdin.readline

n = int(input())
word = list(input().rstrip())

for i in range(len(word)):
    if ord(word[i]) >= 65:
        word[i] = ' '

word = list(map(int, ''.join(ch for ch in word).strip().split()))
print(sum(word))