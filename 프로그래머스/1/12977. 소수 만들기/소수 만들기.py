def solution(nums):
    answer = -1
    li = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                li.append(nums[i]+nums[j]+nums[k])     
    res = []
    for x in li:
        count = 0
        for y in range(2,x+1):
            if x % y == 0:
                count += 1
        if count == 1:
            res.append(x)
    
    return len(res)