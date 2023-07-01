import sys
input = sys.stdin.readline

def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    dict = {}

    for term in terms:
        term = term.split()
        dict[term[0]] = int(term[1])
    
    i = 1
    for privacy in privacies:
        privacy = privacy.split()
        privacy_term = list(map(int, privacy[0].split('.')))
        privacy_type = privacy[1]
        
        long = dict[privacy_type]
        
        tmp = privacy_term[:]
        tmp[1] += long
        if tmp[1] > 12:
            tmp[0] += 1
            tmp[1] -= 12
        print(tmp)

        if (today[0] > tmp[0]) or ((today[0] == tmp[0]) and (today[0 + 1] > tmp[0 + 1])) or ((today[0] == tmp[0]) and (today[0 + 1] == tmp[0 + 1]) and (today[0 + 2] >= tmp[0 + 2])):
            answer.append(i)
                
        i += 1
    
    print(answer)  

today_ = "2020.01.01"
terms_ = ["Z 3", "D 5"]
privacies_ = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

solution(today_, terms_, privacies_)