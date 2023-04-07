for _ in range(int(input())):
    scores = list(map(int, input().split()))
    
    # 슬라이싱 이용
    avg = sum(scores[1:]) / scores[0]
    cnt = 0

    for score in scores[1:]:
        if score > avg:
            cnt += 1

    per = (cnt / scores[0]) * 100

    print(f'{per:.3f}%')