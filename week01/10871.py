# n개의 수를 입력받고 a에 저장
# a에서 x보다 작은 수 출력

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if x > i:
        print(i, end=' ')