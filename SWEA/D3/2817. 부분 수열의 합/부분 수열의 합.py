from itertools import combinations

T = int(input())
for ts in range(1,T+1):
    N, K = map(int,input().split()) # N: 수열 개수, K: 찾고자 하는 수
    li = list(map(int,input().split())) # 수열 값들의 리스트
    count = 0
    for i in range(1,N+1):
        for comb in combinations(li,i):
            if sum(comb) == K:
                count +=1 

    print(f"#{ts} {count}")