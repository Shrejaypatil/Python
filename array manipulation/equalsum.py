
'''
Find the number of subarrays that sum to a given value k

# Input
nums = [1, 1, 1]
k = 2

# Output
count = 2


'''


def naive(arr):
    
    sum1 = 0
    count = 0
    
    for i in range(len(arr)):
        
        for j in range(len(arr)):
            
            sum1 = sum(arr[i : j + 1])
            
            if(sum1 == k):
                
                count += 1
                sum1 = 0
                
    return count


nums = [1, 1, 1]
k = 2

print("The subarrays whose sum is equal to target are: ", naive(nums))

