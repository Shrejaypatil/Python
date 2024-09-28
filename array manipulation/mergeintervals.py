'''
 Given a list of intervals, merge all overlapping intervals
 
 # Input
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Output
merged_intervals = [[1, 6], [8, 10], [15, 18]]


'''


def naive(arr):
    
    arr.sort(key = lambda x : x[0])
    
    ans = []
    
    for i in range(len(arr)-1):
        
        temp = []
        
        if arr[i][1] > arr[i+1][0] and arr[i][0]!=0:
            
            temp.append(arr[i][0])
            temp.append(arr[i+1][1])
            
            ans.append(temp)
            arr[i+1] = [0,0]
            
        else :
            
            if arr[i][0]!=0 :
                ans.append(arr[i])
        
    ans.append(arr[i+1])
    return ans
            
                   


intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]


print(naive(intervals))