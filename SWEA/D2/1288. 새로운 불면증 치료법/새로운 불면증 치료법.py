T = int(input())

for ts in range(1,T+1):
    num = int(input())
    count = 0
    li = []
    k = 1
    while count != 10:
        temp = num * k
        result = temp
        while temp>0:
            li.append(temp%10)
            temp//=10
        
        k += 1
        count = len(set(li))
    print(f"#{ts} {result}")