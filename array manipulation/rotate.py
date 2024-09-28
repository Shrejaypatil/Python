'''
Rotate an array to the right by k steps.

# Input
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

# Output
rotated_array = [5, 6, 7, 1, 2, 3, 4]


'''


def naive(arr,k):
    
    n = len(arr)
    
    temp = [0]*n
    
    for i in range(len(arr)):
        
        temp[(i+k)%n] = arr[i]
        
    return temp


def optimized(arr,k):
    
    n = len(arr)
    k = k % n
    
    l = arr[-k:] + arr[:-k] 
    
    return l

nums = [1, 2, 3, 4, 5, 6, 7]
k = 4


print("The modified arr using naive : ", naive(nums,k))
print("The modified arr using naive : ", optimized(nums,k))