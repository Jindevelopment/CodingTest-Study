T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = []
    for k in range(num):
        row = [1] * (k+1)
        for j in range(1,k):
            row[j] = li[k-1][j-1]+li[k-1][j]
        li.append(row)
    print(f"#{ts}")
    for x in range(num):
        for y in li[x]:
            print(y,end=" ")
        print()