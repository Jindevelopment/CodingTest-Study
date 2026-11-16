T = int(input())

for ts in range(1,T+1):
    st = input()
    answer = ""
    for i in st:
    	if i not in ["a","e","i","o","u"]:
            answer += i
    print(f"#{ts} {answer}")
        