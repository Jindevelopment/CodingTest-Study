T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = []
    print(f"#{ts}")
    #배열 입력 받기
    for i in range(num):
        row = list(map(int,input().split()))
        li.append(row)

    for p in range(num):
        r90 = ""
        r180 = ""
        r270 = ""
        for k in range(num-1,-1,-1):
            r90 += str(li[k][p])
        r90 += " "
        for j in range(num-1,-1,-1):
            r180 += str(li[num-p-1][j])
        r180 += " "
        for z in range(num):
            r270 += str(li[z][num-p-1])
        r270 += " "
        print(r90 + r180 + r270)
    	    
   
    