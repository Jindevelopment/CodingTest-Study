for ts in range(1,11):
    length = int(input())
    li = list(map(int,input().split()))
    num = int(input())
    x = input().split("I")
    temp = []

    for i in range(1, len(x)):
        temp.append(list(map(int, x[i].split())))
    
    for i in range(num):
        for j in range(temp[i][1]):
            li.insert(temp[i][0]+j,temp[i][2+j])
    
    print(f"#{ts} ",end="")
    print(*li[:10],end=" ")
    print()
