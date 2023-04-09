import math

# 1.
# x, y, w, h = map(int, input().split())
# dist = [x, y, w-x, h-y]
# print(min(dist))

# 2. 
x, y, w, h = map(int, input().split())
dist = [x, y, w-x, h-y]
min = 1000 # 조건 w,h <= 1000

for i in dist:
    if i < min:
        min = i

print(min)