def solution(arr):
    answer = 0

    temp = arr[0]
    
    for i in range(1,len(arr)):
        res = gcd(temp,arr[i])
        temp = (temp * arr[i]) // res
                  
    
    return temp

def gcd(a,b):
    temp = 0
    if a < b:
        for j in range(1,b+1):
            if a%j==0 and b % j ==0:
                temp = j
    elif a > b:
        for k in range(1,a+1):
            if a%k==0 and b % k ==0:
                temp = k
    else:
        temp = a
    
    return temp
