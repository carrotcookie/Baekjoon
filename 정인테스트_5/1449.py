import sys
input = sys.stdin.readline

n, l = map(int, input().split())
leak_pos = list(map(int, input().split()))
leak_pos.sort()
ans = 0

pivot = leak_pos[0]

for pos in leak_pos[1:]:
    if pos >= pivot + l:
        ans += 1
        pivot = pos

print(ans + 1)