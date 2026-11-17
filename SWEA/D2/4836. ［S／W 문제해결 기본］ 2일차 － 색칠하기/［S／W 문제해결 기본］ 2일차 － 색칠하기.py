T = int(input())

for ts in range(1,T+1):
    li = [ [0] * 10 for N in range(10)]
    
    num = int(input())
    
    for i in range(num):
        startx, starty, endx, endy, value = map(int,input().split())
        for x in range(startx,endx+1):
            for y in range(starty,endy+1):
                li[x][y]+=value
    
    count = 0
    
    for u in range(10):
        for v in range(10):
            if li[u][v]==3:
                count+=1
    
    print(f"#{ts} {count}")