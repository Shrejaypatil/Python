'''
Return an array where each element is the product of all elements except itself.

# Input
nums = [1, 2, 3, 4]

# Output
result = [24, 12, 8, 6]


'''

def naive(arr):
    l = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i!=j :
                product *= arr[j]
        l.append(product)
        
    return l
        
        

nums = [1, 2, 3, 4]


print("The modified arr with naive : ", naive(nums))