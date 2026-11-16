T = int(input())

for ts in range(1,T+1):
    a, b = map(int,input().split())
    li = list(map(int,input().split()))
    for i in range(b):
        temp = li[0]
        for k in range(a-1):
            li[k]=li[k+1]
        li[a-1]=temp
    print(f"#{ts} {li[0]}")