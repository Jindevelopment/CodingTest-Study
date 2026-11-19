T = int(input())

for ts in range(1,T+1):
    N, K = map(int, input().split())
    li = []
    answer = 0
    for i in range(N):
        row = list(map(int,input().split()))
        li.append(row)
    
    #가로 검사
    for x in range(N):
        for y in range(N-K+1):
            if y==0:
            	if sum(li[x][y:y+K])==K and li[x][y+K] == 0:
                	answer += 1
            elif y == N-K:
                if li[x][y-1]==0 and sum(li[x][y:y+K])==K:
                    answer+=1
            else:
                if li[x][y-1]==0 and li[x][y+K] == 0 and sum(li[x][y:y+K])==K:
                    answer += 1
                    
    #세로 검사
    for u in range(N): #열
        for v in range(N-K+1):
            total = 0
            for j in range(v,v+K):
            	total += li[j][u]
            if v==0:
            	if total==K and li[v+K][u] == 0:
                	answer += 1
            elif v == N-K:
                if li[v-1][u]==0 and total==K:
                    answer+=1
            else:
                if li[v-1][u]==0 and li[v+K][u] == 0 and total==K:
                    answer += 1
    print(f"#{ts} {answer}")