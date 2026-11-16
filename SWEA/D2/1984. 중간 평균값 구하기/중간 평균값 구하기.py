T = int(input())
for ts in range(1,T+1):
    li = list(map(int,input().split()))
    li.sort()
    li.pop()
    li.pop(0)
    total = 0
    for k in li:
        total+=k
    print(f"#{ts} {int(round(total/len(li),0))}")
            