'''
Return a list of duplicate elements from the array.

# Input
nums = [4, 3, 2, 7, 8, 2, 3, 1]

# Output
duplicates = [2, 3]


'''

def naive(arr):
    
    
    l = []
    ans = []
    
    for i in arr:
        
        if i not in l:
            
            l.append(i)            
            
        else : 
            
            ans.append(i)
    
    
    return ans

nums = [4, 3, 2, 7, 8, 2, 3, 1]

print("The duplicates present are : ",naive(nums))