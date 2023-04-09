for _ in range(int(input())):
    r, s = input().split()
    
    for ch in s:
        print(ch * int(r), end = '')
    
    print()