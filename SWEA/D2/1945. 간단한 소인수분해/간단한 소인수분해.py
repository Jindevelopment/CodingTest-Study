T = int(input())
for ts in range(1,T+1):
    print(f"#{ts} ",end="")
    temp = int(input())
    li = [0,0,0,0,0]
    while temp%2==0:
        li[0]+=1
        temp//=2
    while temp%3==0:
        li[1]+=1
        temp//=3
    while temp%5==0:
        li[2]+=1
        temp//=5
    while temp%7==0:
        li[3]+=1
        temp//=7
    while temp%11==0:
        li[4]+=1
        temp//=11
    for k in li:
        print(k,end=" ")
    print()
    
