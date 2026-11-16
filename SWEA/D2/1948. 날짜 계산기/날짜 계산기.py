T = int(input())
month = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [31,28,31,30,31,30,31,31,30,31,30,31]

for ts in range(1,T+1):
    li = list(map(int,input().split()))
    print(f"#{ts} ",end="")
    if li[0]==li[2]:
        print(li[3]-li[1]+1)
    else:
        sum = 0
        sum += days[li[0]-1]-li[1] #30 - 17 = 13
        sum += li[3]+1
        if li[2]-li[0]>=2: 
            for k in range(li[0]+1,li[2]):
                sum+=days[k-1]
        print(sum)