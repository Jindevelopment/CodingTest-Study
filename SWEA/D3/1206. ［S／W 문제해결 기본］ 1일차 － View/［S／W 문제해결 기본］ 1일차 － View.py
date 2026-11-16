for i in range(1,11):
    building = int(input())
    li = list(map(int,input().split()))
    answer = 0
    for k in range(2,building-2):
        left = max(li[k-2],li[k-1])
        right = max(li[k+2],li[k+1])
        if li[k]>left and li[k]>right:
            answer += li[k] - max(left,right)
    print(f"#{i} {answer}")