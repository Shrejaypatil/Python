'''
Find two numbers in the array such that their sum equals a specific target. Return their indices.

# Input
nums = [2, 7, 11, 15]
target = 9

# Output
indices = [0, 1]

'''


'''
as it is specified in the question to find pair of numbers and return its index, also that they may not
be a contigous one too

'''

# naive approach


def naive(arr):

    i1 = 0
    i2 = 0

    for i in range(0, len(arr)):

        sum = 0

        for j in range(i+1, len(arr)):

            sum = arr[i] + arr[j]

            if sum == target:

                i1 = i
                i2 = j
                
                return i1,i2

def two_sum(nums, target):
    # Create a dictionary to store the complement and index
    hash_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in the map, return the indices
        if complement in hash_map:
            return [hash_map[complement], i]
        
        # Store the current number and its index in the hash map
        hash_map[num] = i

# Example Input
nums = [2, 7, 11, 15]
target = 9

arr = [15, 11, 2, 7]

target = 9

# Output
result = two_sum(nums, target)
print(result)  # Output: [0, 1]


print("index of numbers whose sum is equal to target are : ", naive(arr))

