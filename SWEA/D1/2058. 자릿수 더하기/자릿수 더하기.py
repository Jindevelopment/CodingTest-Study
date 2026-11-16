a = int(input())
res = 0
while a!=0:
    res += a%10
    a //=10
print(res)