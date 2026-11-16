for ts in range(1,11):
    num = int(input())
    li = list(map(int,input().split()))
    i = 1
    while li[7]>0:
        if i >5:
            i = 1
        else:
            temp = li[0]-i
            for k in range(7):
                li[k] = li[k+1]
            li[7]= temp
            i+=1
    li[7] = 0
    print(f"#{ts} ",end="")
    for j in range(8):
        print(li[j],end=" ")
    print()