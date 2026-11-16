T = int(input())

for ts in range(1,T+1):
    N, K = map(int,input().split())
    li = []
    
    for i in range(N):
        rows = list(map(int,input().split()))
        li.append(rows)
    
    count = 0
    
    #행 처리
    for x in range(N):
        for y in range(N-K+1):
            if N==K:
                if sum(li[x][y:y+K])==K:
                    count+=1
            elif y==N-K:
                if li[x][y-1]==0 and sum(li[x][y:y+K])==K:
                    count+=1
            elif y > 0:
                if li[x][y-1]==0 and sum(li[x][y:y+K])==K and li[x][y+K]==0:
                    count +=1
            elif y==0:
                if sum(li[x][y:y+K])==K and li[x][y+K]==0:
                    count +=1
                
    #열 처리
    for u in range(N):
        for v in range(N-K+1):
            total = sum(li[j][u] for j in range(v,v+K)) 
            if N==K:
                if total==K:
                    count+=1
            elif v==N-K:
                if li[v-1][u]==0 and total==K:
                    count+=1
            elif v > 0:
                if li[v-1][u] == 0 and total==K and li[v+K][u]==0:
                    count+=1
            elif v == 0:
                if total== K and li[v+K][u]==0:
                    count+=1
                    
    
    print(f"#{ts} {count}")
       
                
    