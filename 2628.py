x,y=map(int, input().split())   # 종이 가로세로 길이
t  = int(input())               # 몇번 자를건지
list_1 = [0, x]                 # 세로로 자를 위치를 추가할거임
list_2 = [0, y]                 # 가로로 자를 위치를 추가할거임

for i in range(t):
    dir, pos = map(int, input().split())
    
    if dir == 0:
        list_2.append(pos)      # 가로로 자를 위치 추가
    elif dir == 1:
        list_1.append(pos)      # 세로로 자를 위치 추가

# 리스트 정렬 후 이웃끼리의 차이가 가장 큰것끼리 곱하면 넓이임
list_1.sort()   
list_2.sort()
max1, max2 = 0, 0

for i in range(len(list_1) - 1):
    if list_1[i+1]-list_1[i] > max1:
        max1 = list_1[i+1]-list_1[i]
for i in range(len(list_2) - 1):
    if list_2[i+1]-list_2[i] > max2:
        max2 = list_2[i+1]-list_2[i]

print(max1 * max2)