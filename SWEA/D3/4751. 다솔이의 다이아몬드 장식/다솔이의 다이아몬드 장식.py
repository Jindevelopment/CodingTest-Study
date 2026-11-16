T = int(input())

for ts in range(1,T+1):
    temp = input().strip()
    length = len(temp)
    
    line1 = "..#." * length + "."
    line2 = ".#"*(length*2) +"."
    line3= "#."
    for i in range(length):
        line3+=temp[i]
        line3+=".#."
    line3 = line3[:-1]
    line4=".#"*(length*2) +"."
    line5 = "..#." * length + "."
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

    
    