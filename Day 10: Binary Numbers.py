def get_length(arr):
    count = 0
    result = 0 
    k = len(arr)
    for i in range(0, k):
        if (arr[i] == '0'): 
            count = 0 
        else: 
            count+=1 
            result = max(result, count) 
    return result  

n = int(input())
bi = list(bin(n)[2:])
print(get_length(bi))
