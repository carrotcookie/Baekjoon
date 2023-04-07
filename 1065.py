n = input()
count = 0

if int(n) < 100:    # 두자리수까지는 모두 한수이다
    print(n)
else:               # 세자리부터 검사실시
    for i in range(100, int(n)+1): # 100부터 현재수까지
        isRight = True

        for j in range(1, len(str(i))-1):
            if (int(str(i)[j-1]) - int(str(i)[j])) != (int(str(i)[j]) - int(str(i)[j+1])): # 인덱스별 등차가 아니면 탈출
                isRight = False
                break

        if isRight:
            count += 1
    
    print(count + 99)