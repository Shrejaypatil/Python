'''
Recursion: A coding concept where a function calls itself, that is inside the function defination there is a call for itself, but to handle its infinite run we have to specify a base condition always.


factorial example: 

5! = 5 * 4 * 3 * 2 * 1 = 120

we know 1! is always 1
'''

def fact(num):
    if(num == 1):
        return 1
        
    return num*fact(num-1)
    
print(fact(5))
