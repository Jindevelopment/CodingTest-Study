T = int(input())

for ts in range(1,T+1):
    str1 = input()
    str2 = input()
    length = len(str1)
    temp = []
    for i in str1:
        temp.append(i)
    temp = list(set(temp))
    length = len(temp)
    res = [0] * length
    for j in str2:
        for z in range(length):
            if temp[z] == j:
                res[z] +=1
    
    print(f"#{ts} {max(res)}")