T = int(input())


for ts in range(1,T+1):
    money = int(input())
    li = [0] * 8
    temp = [50000,10000,5000,1000,500,100,50,10]
    for i in range(len(temp)):
        li[i]+=money//temp[i]
        money %= temp[i]
        
    print(f"#{ts}")
    for k in li:
        print(k,end=" ")
    print()
        
        