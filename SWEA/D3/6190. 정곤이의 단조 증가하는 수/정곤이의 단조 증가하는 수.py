T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = list(map(int,input().split()))
    
    temp1 = []
    temp2 = []
    for i in range(num):
        for k in range(i+1,num):
            temp1.append(str(li[i]*li[k]))
    
    for x in temp1:
        count = 0
        for y in range(len(x)-1):
            if x[y] > x[y+1]:
                count = 1
                break
        if count == 0:
            temp2.append(int(x))
    
    if len(temp2) == 0:
        print(f"#{ts} -1")
    else:
        print(f"#{ts} {max(temp2)}")
    
    