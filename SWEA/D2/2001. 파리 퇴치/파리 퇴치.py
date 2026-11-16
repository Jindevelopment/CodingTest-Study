T = int(input())
for ts in range(1,T+1):
    a,b=map(int,input().split())
    temp = [[0]*a for i in range(a)]
    for k in range(a):
        li = list(map(int,input().split()))
        for j in range(a):
            temp[k][j]=li[j]
    maxy= []
    for x in range(a-b+1): #0~3
        for y in range(a-b+1): #0~3
            total = 0
            for u in range(b):
                for v in range(b):      
                    total += temp[x+u][y+v]
            maxy.append(total)
            
    print(f"#{ts} {max(maxy)}")