# 1. 
# a = int(input())
# b = list(map(int, input()))

# c = [0, 0, 0]

# c[2] = a * b[0]
# c[1] = a * b[1]
# c[0] = a * b[2]

# print(c[0], c[1], c[2], 100*c[2]+10*c[1]+c[0], sep = '\n')

# 2.
a = int(input())
b = input()

c = a * int(b)
c2 = a * int(b[0])
c1 = a * int(b[1])
c0 = a * int(b[2])

print(c0, c1, c2, c, sep='\n')