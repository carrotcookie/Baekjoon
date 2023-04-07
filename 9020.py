for _ in range(int(input())):
    n = int(input())

    # n//2 가 짝수인지 홀수인지 나눠서 2씩 감소하면서 하면 더 빠를지도?
    for i in range(n//2, 1, -1):        # 입력받은 수를 절반으로 쪼개고 1씩 감소
        isPrimeNum = True

        for j in range(2, i):           # i가 소수인지 검사
            if i % j == 0:
                isPrimeNum = False
                break

        if isPrimeNum:                  # i가 소수라면
            for j in range(2, n-i):     # n-i에 대해서도 소수인지 검사
                if (n-i) % j == 0:
                    isPrimeNum = False
                    break

            if isPrimeNum:              # n-i도 소수라면
                print(i, n-i)           # i, n-i 출력
                break