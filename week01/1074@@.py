n,r,c = map(int, input().split())
count = 0

# 8 x 8 이면 4 x 4 짜리로 1,2,3,4분면 나누고 좌표가 어디영역에 있는지에 따라 카운팅
# 카운팅 후에 r,c 를 감소시키고 4 x 4 를 2 x 2로 나누어 1,2,3,4분면 다시 따져줌
while n > 1:
    size = 2 ** (n-1)

    if r < size and c < size:
        pass
    elif r < size and c >= size:
        count += size ** 2
        c -= size
    elif r >= size and c < size:
        count += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:
        count += size ** 2 * 3
        r -= size
        c -= size
    n -= 1

# 2 x 2가 되었을 때는 직접 카운팅해줘야함
if r == 0 and c == 0:
    print(count)
elif r == 0 and c == 1:
    print(count + 1)
elif r == 1 and c == 0:
    print(count + 2)
else:
    print(count + 3)