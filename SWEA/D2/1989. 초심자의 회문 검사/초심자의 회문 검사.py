T = int(input())

for ts in range(1, T+1):
    li = input().strip()
    li1 = []
    li2 = []
    for i in li:
        li1.append(i)
    for k in range(len(li)-1,-1,-1):
        li2.append(li[k])
    
    count = 1
    for j in range(len(li)):
        if li1[j] != li2[j]:
            count = 0
            
    print(f"#{ts} {count}")