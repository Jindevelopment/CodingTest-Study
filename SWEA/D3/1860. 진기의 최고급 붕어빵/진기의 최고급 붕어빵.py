T = int(input())

for ts in range(1,T+1):
    N, M, K = map(int,input().split())  # N: 손님 수 / M,K :  0 ~ M초 사이에 만들 수 있는 붕어빵의 수 K
    li = list(map(int,input().split()))
    li.sort()
    
    last_guest = li[-1] #제일 마지막에 온 손님
    
    default = "Possible"
    
    temp = [0] * 11111
    for i in range(M,11111,M): # 각 초에 생성된 붕어빵의 수
        temp[i] += K
    
    for k in li:
        if sum(temp[:k+1])<=0:
            default = "Impossible"
            break
        else:
            for j in range(M,k+1):
                if temp[j]>0:
                    temp[j]-=1
                    break
            
    
    print(f"#{ts} {default}")
        
    