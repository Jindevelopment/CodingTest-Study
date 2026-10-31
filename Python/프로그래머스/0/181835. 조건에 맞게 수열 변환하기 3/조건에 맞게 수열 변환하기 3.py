def solution(arr, k):
    answer = []
    
    answer = [i*k if k%2 == 1 else i+k for i in arr ]
        
    return answer