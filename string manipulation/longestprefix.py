
'''
Find the Longest Common Prefix


Write a function to find the longest common prefix amongst an array of strings.


strs = ["flower", "flow", "floght"]
print(longest_common_prefix_naive(strs))  # Output: "flo"


'''


strs = ["flower", "flow", "floght"]

prefix = strs[0]

for i in range(1, len(strs)):
    while strs[i].find(prefix) != 0:
        prefix = prefix[:-1]
            
    
print(prefix)
        
