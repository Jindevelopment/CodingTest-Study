T = int(input())

alien = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
res = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}

for ts in range(1,T+1):
    problem, num = input().split()
    num = int(num)
    print(problem)
    
    temp = [0] * 10
    li = input().split()
    for i in range(num):
        temp[alien[li[i]]] += 1
    
    for j in range(len(temp)):
        for k in range(temp[j]):
            print(res[j],end=" ")
    print()
    
        
    
    