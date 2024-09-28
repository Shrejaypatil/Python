

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

# Input
nums = [3, 0, 1]

# Output
missing_number = 2

 
'''

arr = [3 , 0 , 1]

# approach 1 (naive) : sort list and iterate over it and assume next number to be +1 always if not its missing


def naive(arr):
    
    arr.sort()
    
    ans = 0
    
    for i in range(0,len(arr)):
        
        if arr[i+1] != arr[i]+1:
            
            ans = arr[i] + 1
            break;
            
    return ans


def optimized(arr):
    
    n = len(arr)
    actualSum = n * (n+1) // 2

    givenSum = sum(arr)
    
    return actualSum - givenSum


print("The missing number is : ", naive(arr))
print("The missing number is : ", optimized(arr))
            
            