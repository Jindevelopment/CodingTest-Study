def solution(park, routes):
    answer = []
    x, y = 0,0
    #1. S의 위치 좌표 찾기(x,y)
    for i in range(len(park)):
        for k in range(len(park[i])):
            if park[i][k]=="S":
                x,y=i,k
                break
                
    #명령어 실행
    for move in routes:
        where, distance = move.split() # 어디로 이동할 것인지: where
        distance = int(distance) # 이동할 거리 : distance
        
        #E인 경우(우)
        if where == "E":
            possible = 1
            for u in range(distance):
                if y+1+u >= len(park[x]) or park[x][y+1+u] == "X":
                    possible = 0
                    break
            if possible:
                y = y+distance
        
        #W인 경우(좌)
        if where == "W":
            possible = 1
            for v in range(distance):
                if y-1-v < 0 or park[x][y-1-v] == "X":
                    possible = 0
                    break
            if possible:
                y = y-distance
        
        
        #S인 경우(하)
        if where == "S":
            possible = 1
            for a in range(distance):
                if a+1+x >= len(park) or park[a+1+x][y] == "X":
                    possible = 0
                    break
            if possible:
                x = x + distance
        
        
        #N인 경우(상)
        if where == "N":
            possible = 1
            for b in range(distance):
                if x-b-1 < 0 or park[x-b-1][y] == "X":
                    possible = 0
                    break
            if possible:
                x = x - distance
            
        
    
    return [x,y]