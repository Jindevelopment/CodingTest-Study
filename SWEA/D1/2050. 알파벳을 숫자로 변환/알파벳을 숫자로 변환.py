a = input().upper()
eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in a:
    print(eng.find(i)+1,end=" ")