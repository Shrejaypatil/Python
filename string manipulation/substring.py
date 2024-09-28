

'''

Given two strings s and t, return the minimum window in s which will
contain all the characters in t.


s = "ADOBECODEBANC"
t = "ABC"

'''

s = "abcabcbb"

ans = []

for i in range(len(s)):
    
    for j in range(len(s)):
        
        print(s[i:j+1])
            
            


# print("The substring having matching all characters and is smallest is ")
