# 1. 메모리 초과
# import sys
# import itertools
# input = sys.stdin.readline

# # anta, tica => 5개
# n, k = map(int, input().split())
# alphabet = [chr(i) for i in range(97, 123)]
# arr = []
# more_learn = []
# already_learn = ['a', 'c', 'i', 'n', 't']
# answer = 0

# if k - 5 > 0:
#     more_learn = list(itertools.combinations(alphabet, k - 5))

# for _ in range(n):
#     tmp = input().rstrip()
#     arr.append(''.join(sorted(tmp[4:len(tmp) - 4])))

# if k < 5:
#     print(0)
# else:
#     for learn in more_learn:
#         learn =  already_learn + [ch for ch in learn if ch not in already_learn]
#         tmp = 0

#         for word in arr:
#             word_len = len(word)
#             count = 0

#             for ch1 in learn:
#                 for ch2 in word:
#                     if ch1 == ch2:
#                         count += 1
#                     if count == word_len:
#                         break
#                 else:
#                     continue
#                 break
#             else:
#                 continue
#             tmp += 1
   
#         answer = max(answer, tmp)

#     print(answer)

###############################################################################################################################

# 2. 메모리 초과
# import sys
# import itertools
# input = sys.stdin.readline

# # anta, tica => 5개
# n, k = map(int, input().split())
# words = [input().rstrip() for _ in range(n)]
# alphabet = [chr(i) for i in range(97, 123)]
# more_learn_comb = []
# answer = 0
# learn = [0] * 26

# if k >= 5:
#     more_learn_comb = list(itertools.combinations(alphabet, k - 5))

#     for more_learn in more_learn_comb:
#         for i in range(26):
#             learn[i] = 0
#         learn[0] = learn[2] = learn[8] = learn[13] = learn[19] = 1

#         tmp = 0

#         for ch in more_learn:
#             learn[ord(ch) - 97] = 1

#         for word in words:
#             count = 0

#             for ch in word:
#                 if learn[ord(ch) - 97] == 1:
#                     count += 1
            
#             if count == len(word):
#                 tmp += 1
        
#         answer = max(answer, tmp)
    
#     print(answer)
# else:
#     print(0)

###############################################################################################################################

# 3. 
import sys
import itertools
input = sys.stdin.readline

def word_to_bit(word):
    tmp = 0

    for ch in word:
        tmp |= 2 ** (ord(ch) - 97)

    return tmp

# anta, tica => 5개
n, k = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
already_learn = word_to_bit('antic')
alphabets = [1 << i for i in range(26) if already_learn & 1 << i == 0]
answer = 0

if k < 5:
    print(0)
else:
    for combination in itertools.combinations(alphabets, k - 5):
        learn = already_learn | sum(combination)
        count = 0 

        for word in words:
            num = word_to_bit(word)

            if learn & num == num:
                count += 1

        answer = max(answer, count)

    print(answer)