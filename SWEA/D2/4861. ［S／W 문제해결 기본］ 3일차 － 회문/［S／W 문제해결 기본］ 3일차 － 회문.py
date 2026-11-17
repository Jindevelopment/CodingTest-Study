T = int(input())

for ts in range(1,T+1):
    N,M = map(int,input().split())
    li = []
    for i in range(N):
        row = input()
        li.append(row)
    
    #가로 검사
    res = ""
    for x in range(N):
        for y in range(N-M+1):
            temp = "".join(li[x][y:y+M])
            if temp == temp[::-1]:
                res = temp
    
    #열
    for u in range(N):
        for v in range(N-M+1):
            temp =""
            for z in range(v,v+M):
                temp += li[z][u]
            if temp==temp[::-1]:
                res = temp
    
    print(f"#{ts} {res}")
                            
            