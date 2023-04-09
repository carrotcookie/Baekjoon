# 1. 처음 했던거
# for _ in range(int(input())):
#     n = int(input())

#     for i in range(n//2, 1, -1):        # 입력받은 수를 절반으로 쪼개고 1씩 감소
#         isPrimeNum = True

#         for j in range(2, i):           # i가 소수인지 검사
#             if i % j == 0:
#                 isPrimeNum = False
#                 break

#         if isPrimeNum:                  # i가 소수라면
#             for j in range(2, n-i):     # n-i에 대해서도 소수인지 검사
#                 if (n-i) % j == 0:
#                     isPrimeNum = False
#                     break

#             if isPrimeNum:              # n-i도 소수라면
#                 print(i, n-i)           # i, n-i 출력
#                 break

# 2.
# 소수 판별
# 가장 가까운 소수의 합으로 표현할 것
# def is_prime_num(n):
#     if n == 1:
#         return False

#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False

#     return True

# for _ in range(int(input())):
#     target_num = int(input())
    
#     a = target_num // 2
#     b = target_num // 2

#     while a > 1:
#         if is_prime_num(a) and is_prime_num(b):
#             print(a, b)
#             break
#         a -= 1
#         b += 1

# 3. 에라토스테네스의 체
def prime_num_sieve(lst, max_num):
    # 2부터 모든 수를 반복
    for i in range(2, max_num + 1):
        # 이미 0이라면 생략
        if lst[i] == 0: continue
        # 해당수의 배수를 전부 0으로 만든다
        for j in range(2*i, max_num+1, i):
            lst[j] = 0

def find_prime_pair(lst, num):
    a, b = num // 2, num // 2
    
    while a > 1:
        if lst[a] != 0 and lst[b] != 0:
            print(lst[a], lst[b])
            break
        a -= 1
        b += 1

num_lst = []
max_input = 0

for _ in range(int(input())):
    tmp = int(input())
    num_lst.append(tmp)

    if tmp > max_input: max_input = tmp

prime_num_lst = [i for i in range(max_input + 1)]

prime_num_sieve(prime_num_lst, max_input)

for num in num_lst:
    find_prime_pair(prime_num_lst, num)