for ts in range(1,11):
    length = int(input())
    li = list(map(int,input().split()))
    num = int(input())
    x = input().split("I")
    temp = []
    for i in x[1:]:
        temp.append(list(map(int,i.strip().split())))
    
    for j in range(num):
        for k in range(temp[j][1]):
            li.insert(temp[j][0]+k,temp[j][2+k])
    
    print(f"#{ts} ",end="")
    for z in range(10):
        print(li[z], end = " ")
    print()
    