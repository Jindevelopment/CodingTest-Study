T = int(input())
for ts in range(1,T+1):
    count = int(input())
    li = [0] * count
    temp = list(map(int,input().split()))
    for k in range(count):
        li[k] = temp[k]
    print(f"#{ts}",end=" ")
    li.sort()
    for z in li:
        print(z,end=" ")
    print()
        