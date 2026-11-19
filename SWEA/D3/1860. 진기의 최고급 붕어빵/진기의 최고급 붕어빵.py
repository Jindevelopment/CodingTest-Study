T = int(input())

for ts in range(1,T+1):
    N,M,K = map(int,input().split())
    guest = list(map(int,input().split()))
    guest.sort()
    
    li =[0] * 11112
    for i in range(M,11112,M): # 각 초마다 붕어빵 생성
    	li[i] = K
    res = 1
    for j in guest:
        if sum(li[0:j+1])>=1:
            for k in range(0,j+1,M):
                if li[k]!=0:
                    li[k]-=1
                    break
        else:
            res = 0
            print(f"#{ts} Impossible")
            break
    if res == 1:
        print(f"#{ts} Possible")
                
            
    
        
    	