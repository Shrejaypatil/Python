

'''
create  a dict to get frequency of items present in a list

'''



lst = [1,1,2,2,2,3,3,3,3,4,2]


dict = {}


for i in lst:
    
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1
    
    
print(dict)