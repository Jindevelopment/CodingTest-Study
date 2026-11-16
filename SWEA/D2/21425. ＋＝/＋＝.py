T = int(input())

for ts in range(1,T+1):
    a, b, N = map(int,input().split())
    
    count = 0
    total = 0
    while total <= N:
        if a < b:
            a+=b
            total = a
            count +=1
        else:
            b+=a
            total = b
            count+=1
 
    print(count)
    
    
    