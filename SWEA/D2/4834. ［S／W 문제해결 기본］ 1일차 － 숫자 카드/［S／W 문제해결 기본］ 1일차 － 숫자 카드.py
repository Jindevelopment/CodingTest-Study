T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = input()
    score = [0] * 10
    for i in range(num):
        score[int(li[i])] += 1
    max_count = max(score)
    max_index_count = 0
    for k in range(len(score)):
        if score[k] == max_count:
            max_index_count += 1
            max_index = k
    if max_index_count == 1:
        max_index = score.index(max_count)
        
    print(f"#{ts} {max_index} {max_count}")