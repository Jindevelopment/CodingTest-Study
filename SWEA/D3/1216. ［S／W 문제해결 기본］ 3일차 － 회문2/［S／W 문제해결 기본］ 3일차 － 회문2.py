for ts in range(1,11):
    num = int(input())
    li = []
    # 100 x 100 배열 초기회
    for i in range(100):
        row = input().strip()
        li.append(row)
    
    # 최대값
    mv = 0
    
    #가로
    for x in range(100):
        for y in range(100):
            for z in range(y+1,100):
                temp = li[x][y:z+1]
                if temp == temp[::-1]:
                    mv = max(len(temp),mv)

            
    #세로
    for u in range(100):
        for v in range(100):
            temp = ""
            for q in range(v,100):
                temp += li[q][u]
                if temp == temp[::-1]:
                    mv = max(mv,len(temp))
                 
    print(f"#{num} {mv}")