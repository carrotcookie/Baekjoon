# 1.
n = int(input())
arr = list(map(int, input().split()))
result = [] # 결과값 저장
temp = [] # 0 ~ n-1 의 인덱스를 모든 경우의 수로 저장

def recursive(cnt):
    if cnt == n:
        result.append(sum(abs(arr[temp[i]] - arr[temp[i + 1]]) for i in range(n - 1)))
        return
    
    for i in range(n):
        # 해당 인덱스가 이미 없을때만 -> 중복제외
        if i not in temp:
            temp.append(i)
            recursive(cnt + 1)
            # 전부 진행했으면 비워줌
            temp.pop()

recursive(0)
print(max(result))