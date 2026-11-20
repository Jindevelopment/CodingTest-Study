from itertools import combinations

T = int(input())

for ts in range(1,T+1):
    N, L = map(int,input().split()) # N : 후보군 수, L: 제한 칼로리

    #점수와 칼로리 배열 등록
    score_cal = []

    # 초기 사전 설정
    for i in range(N):
        x, y = map(int,input().split())
        score_cal.append((x,y))

    res = []
    # 뒤에서부터 거꾸로 내려오면서 combination으로 찾아서
    # 섞었을 때 칼로리의 합이 1000 이하인 경우 그 점수 기록
    for k in range(1,N+1):
        for comb in combinations(score_cal,k):
            scores, cals = zip(*comb)
            if sum(cals) <= L:
                res.append(sum(scores))

    print(f"#{ts} {max(res)}")