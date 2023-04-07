for i in range(int(input())):
    list = input()
    score = 0
    bonus = 0

    for j in range(len(list)):
        if list[j] == 'O':
            score += (1+bonus)
            bonus += 1
        else:
            bonus = 0
    
    print(score)